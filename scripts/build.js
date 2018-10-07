const { existsSync, writeFileSync } = require('fs')
const { normalize } = require('path')
const { exec } = require('child_process')
const chalk = require('chalk')
const ora = require('ora')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath)) {
    console.error(chalk.red('\n  MACRON ERR: Application must include a macron.config.js config file.\n'))
    process.exit()
  }

  if (!appConfig.appName) {
    console.error(chalk.red('\n  MACRON ERR: macron.config.js must include an appName property.\n'))
    process.exit()
  }

  appConfig.cwd = cwd
  
  const spinner = ora('Starting build process...').start()
  const qualifiedAppName = appConfig.appName.replace(/\s/g, '_')
  const cmdSeperator = (process.platform == 'win32') ? ';' : ':'

  writeFileSync(
    `${cwd}/.builddata`,
    JSON.stringify(appConfig),
    'utf8'
  )
  
  const buildCmd = ['pyinstaller']
  buildCmd.push(`--name=${qualifiedAppName}`)
  buildCmd.push('--workpath=' + normalize(__dirname + '/../cache'))
  buildCmd.push(`--distpath=${cwd}build`)
  buildCmd.push('--specpath=' + normalize(__dirname + '/../cache'))
  buildCmd.push('--hiddenimport=pathlib')
  buildCmd.push('--hiddenimport=json')
  if (appConfig.build.nativeModulesPath)
  buildCmd.push('--distpath=' + normalize(cwd + appConfig.build.nativeModulesPath))
  buildCmd.push('--hiddenimport=_contextmenu')
  buildCmd.push('--hiddenimport=archive')
  buildCmd.push('--hiddenimport=currentwindow')
  buildCmd.push('--hiddenimport=dialog')
  buildCmd.push('--hiddenimport=windowmanager')
  buildCmd.push('--hiddenimport=filesystem')
  buildCmd.push('--hiddenimport=system')
  buildCmd.push(`-p ${
    normalize(__dirname + '/../core') + cmdSeperator +
    normalize(__dirname + '/../core/common') + cmdSeperator +
    // normalize(__dirname + '/../core/windows') + cmdSeperator +
    normalize(__dirname + '/../core/linux')
  }`)
  buildCmd.push(`--add-data=${cwd}/.builddata${cmdSeperator}macron`)
  buildCmd.push(`--add-data=${cwd}public/${cmdSeperator}macron/app`)
  buildCmd.push(`--add-data=${normalize(__dirname + '/../src') + cmdSeperator}macron/core`)
  if (process.platform == 'win32') {  // Windows specific
    buildCmd.push(`--icon=${cwd}public/icons/icon.ico`)
    buildCmd.push('--hiddenimport=clr')
    buildCmd.push(`--add-data=${normalize(__dirname + '/../core/windows/assemblies/MacronWebviewInterop.dll')};macron/assemblies`)
  } else if (process.platform == 'linux') {
    // buildCmd.push('--hiddenimport=GdkPixbuf')
  }
  if (appConfig.build.debugMode) {
    buildCmd.push('--log-level DEBUG')
    buildCmd.push('-c') // console
  }
  buildCmd.push('-w')
  buildCmd.push('-y')
  buildCmd.push(normalize(__dirname + '/../core/') + '__init__.py')

  const buildProcess = exec(buildCmd.join(' '), (err, stdout, stderr) => {
    if (err) {
      console.error(err)
      return
    }

    console.log(stdout)
  })

  buildProcess.stdout.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildProcess.stderr.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildProcess.on('exit', function(data) {
    spinner.stopAndPersist({
      text: chalk.green('\n  Build process complete.\n') + `  Run: ${chalk.cyan('macron start build')} to execute your app.`
    })
  })
}
