const { exec } = require('child_process')
const { existsSync } = require('fs')

const appConfig = process.cwd() + '\\playground\\newtron.config.json'

if (!existsSync(appConfig)) {
  console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
  process.kill()
}

exec(`python ./src/newtron-core.py ${appConfig}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`NEWTRON ERR: ${error}`)

    return
  }

  console.log(stdout)
  console.log(stderr)
})