const {
  basename,
  sep: pathSeperator
} = require('path')
const {
  mkdirSync,
  existsSync,
  writeFileSync
} = require('fs')
const chalk = require('chalk')

/**
 * @todo:
 *     - add .gitignore file
 *     - add .npmignore file
 *     - add package.json file
 *     - add app.bundle.js file
 */

module.exports = function(cwd, appName) {
  if (appName) {
    cwd = cwd + appName + pathSeperator

    try {
      mkdirSync(cwd)
    } catch (err) {
      if (err.code !== 'EEXIST') throw err
    }
  } else {
    appName = basename(cwd)
  }

  const appConfigFilePath = cwd + 'macron.config.js'
  const indexHTMLFilePath = cwd + 'public/index.html'
  const gitIgnoreFilePath = cwd + '.gitignore'
  // const npmIgnoreFilePath = cwd + '.npmignore' // @todo - necessary?
  const packageJsonFilePath = cwd + 'package.json'

  // Macron configuration file
  if (existsSync(appConfigFilePath)) {
    process.stdout.write(
      chalk.hex('#ffa500')('\n    This project is already a macron app.')
      + '\n    Run: ' + chalk.cyan('macron start\n\n')
    )
    process.exit(0)
  }
  
  writeFileSync(
    appConfigFilePath,
    require('./temps/macron-config')(appName)
  )

  // App root HTML file
  if (!existsSync(cwd + 'public')) {
    mkdirSync(cwd + 'public')
    
    if (!existsSync(indexHTMLFilePath))
      writeFileSync(
        indexHTMLFilePath,
        require('./temps/index-html')
      )
  }
  
  // package.json file
  if (!existsSync(packageJsonFilePath))
  writeFileSync(
    packageJsonFilePath,
    require('./temps/package-json')(appName)
  )

  // gitignore file
  if (!existsSync(gitIgnoreFilePath))
    writeFileSync(
      gitIgnoreFilePath,
      require('./temps/gitignore')
    )

  process.stdout.write(
    `\n    ${appName + chalk.green(' created successfully.')}\n    Run: ${chalk.cyan('cd '+appName)}\n\n`
  )
}