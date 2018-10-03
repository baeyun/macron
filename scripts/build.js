const { existsSync, writeFileSync } = require('fs')
const { sep: pathSeperator } = require('path')
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
  appConfig.mainWindow.nativeModulesPath = appConfig.nativeModulesPath.replace("./", "").replace(/[/|\\]/g, pathSeperator)
  
  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')
  const spinner = ora('Starting build process...').start()

  const buildProcess = exec([
    `pyinstaller`,
    `--name=${qualifiedAppName}`,
    `--workpath=app`,
    `--distpath=build`,
    `--specpath=app`,
    `--hiddenimport=clr`,
    `--hiddenimport=pathlib`,
    `--hiddenimport=json`,
    '--log-level DEBUG',
    // '-c',
    '-w',
    '-y',
    'app/__init__.py'
  ].join(' '), (err, stdout, stderr) => {
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
    writeFileSync(
      `${cwd}build/${qualifiedAppName}/.buildinfo`,
      JSON.stringify(appConfig),
      'utf8'
    )

    spinner.stop()
    process.stdout.write(
      chalk.green('\n    Build process complete.')
      + '\n    Run: ' + chalk.cyan('macron start build') + ' to execute your app.\n'
    )
  })
}
