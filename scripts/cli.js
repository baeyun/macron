#!/usr/bin/env node
const { normalize } = require('path')
const { spawn, exec } = require('child_process')
const {
  mkdirSync,
  existsSync,
  readFileSync,
  watchFile
} = require('fs')

const cwd = normalize(process.cwd() + '/')
const [,, ...args] = process.argv

switch(args[0]) {
  /**
   * macron init example-app
   */
  case 'init':
    let appName = args[1]
    
    if (!appName)
      throw new Error("'macron init' requires a valid app name.")

    try {
      mkdirSync(cwd + appName)

      console.log(`macron created ${appName} successfully. Run: cd ${appName}`)
    } catch (err) {
      if (err.code !== 'EEXIST') throw err
    }
    
    break
  
  /**
   * macron start
   */
  case 'start':
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
      'python',
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
    
    break

  /**
   * macron generate-icons
   */
  case 'generate-icons':
    break

  /**
   * macron build
   */
  case 'build':
    break
}

