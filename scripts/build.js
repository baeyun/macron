const { existsSync, writeFileSync } = require('fs')
const { sep: pathSeperator, normalize } = require('path')
const { exec } = require('child_process')
const chalk = require('chalk')
const ora = require('ora')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')
  
  if (!appConfig.name)
    throw new Error('MACRON ERR: macron.config.js must include a name property.')
  
  appConfig.cwd = cwd
  
  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')
  const spinner = ora('Starting build process...').start()

  writeFileSync(
    `${cwd}/.builddata`,
    JSON.stringify(appConfig),
    'utf8'
  )
  
  const buildCmd = ['pyinstaller']
  buildCmd.push(`--name=${qualifiedAppName}`)
  buildCmd.push(`--icon=${cwd}public/icons/icon.ico`)
  buildCmd.push('--workpath=' + normalize(__dirname + '/../cache'))
  buildCmd.push(`--distpath=${cwd}build`)
  buildCmd.push('--specpath=' + normalize(__dirname + '/../cache'))
  buildCmd.push('--hiddenimport=clr')
  buildCmd.push('--hiddenimport=pathlib')
  buildCmd.push('--hiddenimport=json')
  if (appConfig.build.nativeModulesPath) buildCmd.push('--distpath=' + normalize(cwd + appConfig.build.nativeModulesPath))
  buildCmd.push(`--paths=${normalize(__dirname + '/../core')};${normalize(__dirname + '/../core/common')};${normalize(__dirname + '/../core/windows')}`)
  buildCmd.push('--hiddenimport=_contextmenu')
  buildCmd.push('--hiddenimport=archive')
  buildCmd.push('--hiddenimport=currentwindow')
  buildCmd.push('--hiddenimport=dialog')
  buildCmd.push('--hiddenimport=windowmanager')
  buildCmd.push('--hiddenimport=filesystem')
  buildCmd.push('--hiddenimport=system')
  buildCmd.push(`--add-data=${normalize(__dirname + '/../core/windows/assemblies/MacronWebviewInterop.dll')};macron/assemblies`) // Windows specific
  buildCmd.push(`--add-data=${cwd}/.builddata;macron`)
  buildCmd.push(`--add-data=${cwd}public/;macron/app`)
  buildCmd.push(`--add-data=${normalize(__dirname + '/../src')};macron/core`)
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
    spinner.stop()

    process.stdout.write(
      chalk.green('\n    Build process complete.\n')
      + '\n    Run: ' + chalk.cyan('macron start build') + ' to execute your app.\n'
    )
  })
}
