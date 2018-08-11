const { exec } = require('child_process')
const {
  existsSync,
  writeFileSync,
  readFileSync,
  watchFile
} = require('fs')

const appRootPath = process.cwd() + '\\playground\\'

const createConfigJSON = (name, configSrc) => {
  name && writeFileSync(name, JSON.stringify(require(configSrc)))
}

if (!existsSync(appRootPath + "newtron.config.js")) {
  console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
  process.kill()
} else {
  createConfigJSON(appRootPath + "newtron.config.json", appRootPath + "newtron.config.js")
}

const { spawn } = require('child_process')
const newtronCoreInit = spawn('python', ['./src/__init__.py', appRootPath])

const logfilePath = appRootPath + 'newtron-debug.log'

if (existsSync(logfilePath))
  watchFile(logfilePath, { interval: 500 }, (curr, prev) => {
    let from = curr.size - prev.size
    let cont = readFileSync(logfilePath).toString().substr(-from)

    if (cont === '\x1bc')
      process.stdout.write('\x1bc')
    else
      process.stdout.write(cont)
  })

// newtronCoreInit.stdout.on('data', function (data) {
//   console.log(data.toString());
// });

// newtronCoreInit.stderr.on('data', function (data) {
//   console.log(data.toString());
// });

// newtronCoreInit.on('exit', function (code) {
//   console.log('Exited with code ' + code.toString());
// });