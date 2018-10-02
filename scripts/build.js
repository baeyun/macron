const { sep: pathSeperator } = require('path')
const { exec } = require('child_process')
const {
  existsSync,
  writeFileSync,
  readFileSync,
  renameSync
} = require('fs')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')

  if (!appConfig.name)
    throw new Error('MACRON ERR: macron.config.js must include a name property.')

  appConfig.cwd = cwd
  appConfig.name = appConfig.name.replace(/\s/g, '_')
  appConfig.mainWindow.nativeModulesPath = appConfig.nativeModulesPath.replace("./", "").replace(/[/|\\]/g, pathSeperator)

  writeFileSync(
    `${cwd}app/.buildinfo`,
    JSON.stringify(appConfig),
    'utf8'
  )

  // const pyiSpecFileTempPath = `${cwd}app/__init__.spec`
  // const newSpecFilePath = `${cwd}app/${appConfig['name']}.spec`
  // renameSync(pyiSpecFileTempPath, newSpecFilePath)

  const buildProcess = exec([
    'pyinstaller',
    `--name=__init__`,
    `--workpath=${cwd}app`,
    `--distpath=${cwd}build`,
    `--specpath=${cwd}app`,
    `--hiddenimport=clr`,
    `--hiddenimport=pathlib`,
    '--log-level DEBUG',
    '-y',
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
    // renameSync(newSpecFilePath, pyiSpecFileTempPath)
    process.stdout.write(data.toString())
  })
}
