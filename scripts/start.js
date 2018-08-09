const { exec } = require('child_process')
const { existsSync } = require('fs')

const appConfigPath = process.cwd() + '\\playground\\'

if (!existsSync(appConfigPath + "newtron.config.json")) {
  console.log("NEWTRON ERR: Application must include a newtron.config.json config file.")
  process.kill()
}

exec(`python ./src/newtron-core.py ${appConfigPath}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`NEWTRON ERR: ${error}`)

    return
  }

  console.log(stdout)
  console.log(stderr)
})