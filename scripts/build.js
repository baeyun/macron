const { sep: pathSeperator } = require('path')
const { exec } = require('child_process')
const { existsSync, writeFileSync } = require('fs')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')

  if (!appConfig.name)
    throw new Error('MACRON ERR: macron.config.js must include a name property.')

  appConfig.cwd = cwd
  appName = appConfig.name.replace(/\s/g, '_')
  appConfig.mainWindow.nativeModulesPath = appConfig.nativeModulesPath.replace("./", "").replace(/[/|\\]/g, pathSeperator)

  const buildProcess = exec([
    `pyinstaller`,
    `--name=${appName}`,
    `--workpath=${cwd}app`,
    `--distpath=${cwd}build`,
    `--specpath=${cwd}app`,
    `--hiddenimport=clr`,
    `--hiddenimport=pathlib`,
    `--hiddenimport=json`,
    '--log-level DEBUG',
    '-y',
    // '-c',
    '-w',
    'app/__init__.py'
  ].join(' '), (err, stdout, stderr) => {
    if (err) {
      console.error(err)
      return
    }
    
    console.log(stdout)
  })

  buildProcess.stdout.on('data', function(data) {
    process.stdout.write(data.toString())
  })

  buildProcess.stderr.on('data', function(data) {
    process.stdout.write(data.toString())
  })

  buildProcess.on('exit', function(data) {
    writeFileSync(
      `${cwd}build/${appName}/.buildinfo`,
      JSON.stringify(appConfig),
      'utf8'
    )
  })
}
