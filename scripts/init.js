const chalk = require('chalk')
const { mkdirSync } = require('fs')

module.exports = function(cwd, appName) {
  if (!appName)
    throw new Error("MACRON ERR: init requires a valid app name.")

  try {
    mkdirSync(cwd + appName)

    process.stdout.write(
      `\n    ${appName + chalk.green(' created successfully.')}\n    ${chalk.yellow('Run: cd '+appName)}\n\n`
    )
  } catch (err) {
    if (err.code !== 'EEXIST') throw err
  }
}