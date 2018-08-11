const { exec } = require('child_process')
const {
  existsSync,
  writeFileSync,
  readFileSync,
  watchFile
} = require('fs')

const appConfigPath = process.cwd() + '\\playground\\'

const createConfigJSON = (name, configSrc) => {
  name && writeFileSync(name, JSON.stringify(require(configSrc)))
}

if (!existsSync(appConfigPath + "newtron.config.js")) {
  console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
  process.kill()
} else {
  createConfigJSON(appConfigPath + "newtron.config.json", appConfigPath + "newtron.config.js")
}

const { spawn } = require('child_process')
const newtronCoreInit = spawn('python', ['./src/__init__.py', appConfigPath])

const logfilePath = appConfigPath + 'newtron-debug.log'

if (existsSync(logfilePath))
  watchFile(logfilePath, { interval: 500 }, (curr, prev) => {
    let from = curr.size - prev.size

    process.stdout.write(readFileSync(logfilePath).toString().substr(-from))
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