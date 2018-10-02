const { normalize, sep: pathSeperator } = require('path')
const { spawn, execSync } = require('child_process')
const { existsSync } = require('fs')

module.exports = function(cwd, startBuild) {
  const macronRootDir = normalize(__dirname + '/../')
  const appConfigFilePath = cwd + 'macron.config.js'
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')

  const appConfig = require(appConfigFilePath)
  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')

  if (startBuild) {
    let cmd = `${cwd}build/${qualifiedAppName}/${qualifiedAppName}`
    cmd += (process.platform == 'win32') ? '.exe' : ''

    execSync(cmd)
    process.exit(0)
  }

  appConfig.cwd = cwd
  appConfig.mainWindow.nativeModulesPath = appConfig.nativeModulesPath.replace("./", "").replace(/[/|\\]/g, pathSeperator)

  const startProcess = spawn(
    process.platform !==  'linux' ? 'python' : 'python3',
    [
      macronRootDir + 'core/__init__.py',
      // validate appConfig for cli usage
      `"${JSON.stringify(appConfig).replace(/\\/g, '/').replace(/"/g, '\\"')}"`
    ]
  )

  startProcess.stdout.on('data', function(data) {
    process.stdout.write(data.toString())
  })

  startProcess.stderr.on('data', function(data) {
    process.stdout.write(data.toString())
  })

  startProcess.on('exit', function(data) {
    process.stdout.write(data.toString())
  })
}
