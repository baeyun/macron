const { existsSync, readFileSync, mkdirSync, createWriteStream, writeFileSync } = require('fs')
const { normalize } = require('path')
const { exec } = require('child_process')
const archiver = require('archiver')
const chalk = require('chalk')
const ora = require('ora')
// const { addAfter: addAfterObjectItem } = require('json-add-property')
// const stringify = require("json-stringify-pretty-compact")
const { formatBytes } = require('./utils')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath)) {
    console.error(chalk.red('\n  MACRON ERR: Application must include a macron.config.js config file.\n'))
    process.exit()
  }
  
  if (!appConfig.appName)
    console.error(chalk.red('\n  MACRON ERR: macron.config.js must include an appName property.\n'))

  if (!existsSync(cwd+'package.json')) {
    console.error(chalk.red('\n  MACRON ERR: A package.json file is required for deployment.\n  Please include it in your project root.\n'))
    process.exit()
  }

  if (!existsSync(cwd+'LICENSE')) {
    console.error(chalk.red('\n  MACRON ERR: A LICENSE file is required for deployment.\n  Please include it in your project root.\n'))
    process.exit()
  }

  const pkgDotJSON = require(cwd+'package.json')
  let pkgRepoURL = ''
    
  try {
    pkgRepoURL = pkgDotJSON.repository.url.replace(/git\+|\.git/gi, '') + '/raw/master'
  } catch (error) {
    console.error(
      chalk.red(
        '\n  MACRON ERR: package.json must include a GIT repository.url property.'
        + '\n  To turn this project to a GitHub repository, run: git init'
        + '\n  To simply inlcude the repository.url property to your package.json, run: npm init'
        + '\n  Only GitHub repos are currently supported for deployment.\n'
      )
    )
    process.exit()
  }
  
  const qualifiedAppName = appConfig.appName.replace(/\s/g, '_')
  const setupInfo = !existsSync(cwd+'.setupdata')
                  ? JSON.parse(readFileSync(cwd+'.setupdata'))
                  : {'app_name': appConfig.appName}
  setupInfo['app_repo_url'] = pkgRepoURL
  
  // Archive build
  if (!existsSync(cwd+'build') || !existsSync(cwd+'build/' + qualifiedAppName)) {
    console.error(chalk.red('\n  MACRON ERR: A build is required before the deployment step.\n  Run: macron build\n'))
    process.exit()
  }
    
  const spinner = ora('Deploying...').start()
  spinner.stopAndPersist({text: '\n  Archiving latest build...'}).start()

  const platform = process.platform == 'win32' // windows | mac | linux
                 ? 'windows'
                 : process.platform == 'darwin' ? 'mac' : 'linux'
  const platformDistDir = normalize(`${cwd}dist/${platform}/`)
  const buildArchivePath = `${platformDistDir + qualifiedAppName}_${pkgDotJSON['version']}.zip`
  if (!existsSync(cwd+'dist')) {
    mkdirSync(cwd+'dist')
    if (!existsSync(cwd+'dist/'+platform)) {
      mkdirSync(cwd+'dist/'+platform)
    }
  }
  
  const buildArchiveOutputStream = createWriteStream(buildArchivePath)
  buildArchiveOutputStream.on('close', () => {
    
    switch (process.platform) {
      case 'win32':
        setupInfo['latest_windows_dist_url'] = `/dist/windows/${qualifiedAppName}_${pkgDotJSON['version']}.zip`
        break

      case 'darwin':
        setupInfo['latest_mac_dist_url'] = `/dist/mac/${qualifiedAppName}_${pkgDotJSON['version']}.zip`
        break

      case 'linux':
        setupInfo['latest_linux_dist_url'] = `/dist/linux/${qualifiedAppName}_${pkgDotJSON['version']}.zip`
        break
    }
    
    writeFileSync(
      `${cwd}/.setupdata`,
      JSON.stringify(setupInfo),
      'utf8'
    )
    
    spinner.stopAndPersist({
      text: `Archived build to ${formatBytes(archive.pointer())} successfully.\n  Archive location: ${chalk.cyan(buildArchivePath)}`
    }).start()
  })

  const archive = archiver('zip', {
    zlib: { level: 9 } // Sets the compression level.
  })
  archive.on('error', (err) => {
    throw err
  })
  archive.pipe(buildArchiveOutputStream)
  archive.directory(`${cwd}build/${qualifiedAppName}`, qualifiedAppName)
  archive.finalize()

  // Build setup wizard
  spinner.stopAndPersist({
    text: `Building setup wizard...`
  }).start()
  
  // Create {APPNAME}Setup.exe.manifest for --uac-admin to
  // work for -F
  if (!existsSync(__dirname + '/../cache')) mkdirSync(__dirname + '/../cache')
  writeFileSync(
    `${__dirname}/../cache/${qualifiedAppName}Setup.exe.manifest`,
    require('./temps/setupwizard-manifest')(qualifiedAppName),
    'utf8'
  )

  const buildCmd = ['pyinstaller']
  buildCmd.push(`--name=${qualifiedAppName}Setup`)
  buildCmd.push(`--icon=${cwd}public/icons/icon.ico`)
  buildCmd.push(`--workpath=` + normalize(__dirname + '/../cache'))
  // buildCmd.push(`--distpath=${cwd}dist`)
  buildCmd.push(`--specpath=` + normalize(__dirname + '/../cache'))
  buildCmd.push('--hiddenimport=tkinter')
  buildCmd.push('--hiddenimport=tkinter')
  buildCmd.push('--hiddenimport=tkinter')
  buildCmd.push('--hiddenimport=tkinter.messagebox')
  buildCmd.push('--hiddenimport=tkinter.filedialog')
  buildCmd.push('--hiddenimport=json')
  buildCmd.push('--hiddenimport=urllib.request')
  buildCmd.push('--hiddenimport=pygubu')
  buildCmd.push('--hiddenimport=pygubu.builder.ttkstdwidgets')
  buildCmd.push('--hiddenimport=winshell')
  // buildCmd.push('--hiddenimport=PIL.ImageTk')
  // buildCmd.push('--hiddenimport=PIL.Image')
  // buildCmd.push('--hiddenimport=json')
  buildCmd.push(`--add-data=${cwd}/.setupdata;.`)
  buildCmd.push(`--add-data=${normalize(__dirname + '/../')}core/wizard/views;.`)
  buildCmd.push(`--add-data=${cwd}public/icons/icon.ico;.`)
  buildCmd.push(`--add-data=${cwd}LICENSE;.`)
  // buildCmd.push('-m ' + normalize(__dirname + '/../cache/') + qualifiedAppName + 'Setup.exe.manifest')
  buildCmd.push('--uac-admin') // request elevation upon application restart
  // buildCmd.push('--log-level DEBUG')
  // buildCmd.push('-c')
  buildCmd.push('-F')
  buildCmd.push('-w')
  buildCmd.push('-y')
  buildCmd.push(normalize(__dirname + '/../core/wizard/') + '__wizard__.py')

  const buildWizardProcess = exec(buildCmd.join(' '), (err, stdout, stderr) => {
    if (err) {
      console.error(err)
      return
    }
    
    console.log(stdout)
  })

  buildWizardProcess.stdout.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildWizardProcess.stderr.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildWizardProcess.on('exit', function(data) {
    spinner.stopAndPersist({
      text: `Setup wizard built successfully.\n  Run: ${chalk.hex('#ffa500')('macron start wizard')} to test your app\'s setup wizard.`
    })
  })
}
