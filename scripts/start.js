const { normalize } = require('path')
const { spawn } = require('child_process')
const {
  existsSync,
  readFileSync,
  watchFile
} = require('fs')

module.exports = function(cwd) {
  const macronRootDir = normalize(__dirname + '/../')
  const appRootPath = normalize(cwd)
  const appConfigFilePath = appRootPath + 'macron.config.js'
  const logfilePath = appRootPath + 'macron-debug.log'

  // console.log(macronRootDir + 'src/__init__.py')
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')

  const appConfig = require(appConfigFilePath)
  appConfig.appRootPath = appRootPath // required

  // console.log(`python ${macronRootDir}src/__init__.py "${JSON.stringify(appConfig).replace(/"/g, '\\"')}"`)

  const startProcess = spawn(
    process.platform !==  'linux' ? 'python' : 'python3',
    [
      macronRootDir + 'src/__init__.py',
      // validate appConfig for cli usage
      `"${JSON.stringify(appConfig).replace(/\\/g, '/').replace(/"/g, '\\"')}"`
    ]
  )

  startProcess.stdout.on('data', function(data) {
    console.log(data.toString())
  })

  startProcess.stderr.on('data', function(data) {
    console.log(data.toString())
  })

  startProcess.on('exit', function(data) {
    console.log(data.toString())
  })
  
  
  // macron-debug.log to console
  if (existsSync(logfilePath))
    watchFile(logfilePath, { interval: 500 }, (curr, prev) => {
      let from = curr.size - prev.size
      let cont = readFileSync(logfilePath).toString().substr(-from)
  
      if (cont === '\x1bc')
        process.stdout.write('\x1bc')
      else
        process.stdout.write(cont)
    })
}
