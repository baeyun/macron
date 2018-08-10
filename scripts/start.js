const { exec } = require('child_process')
const { existsSync, writeFileSync, readFileSync } = require('fs')

const appConfigPath = process.cwd() + '\\playground\\'

// if (!existsSync(appConfigPath + "newtron.config.json")) {
//   console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
//   process.kill()
// }

const createConfigJSON = (name, configSrc) => {
  name && writeFileSync(name, JSON.stringify(require(configSrc)))
}

if (!existsSync(appConfigPath + "newtron.config.js")) {
  console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
  process.kill()
} else {
  createConfigJSON(appConfigPath + "newtron.config.json", appConfigPath + "newtron.config.js")
}

exec(`python ./src/newtron-core.py ${appConfigPath}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`NEWTRON ERR: ${error}`)

    return
  }

  console.log(stdout)
  console.log(stderr)
})