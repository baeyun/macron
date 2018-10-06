const {
  basename,
  sep: pathSeperator,
  normalize
} = require('path')
const {
  mkdirSync,
  existsSync,
  writeFileSync,
  createReadStream,
  createWriteStream
} = require('fs')
const { execSync } = require('child_process')
const chalk = require('chalk')

module.exports = function(cwd, appName) {
  if (appName) {
    cwd = cwd + appName + pathSeperator

    try {
      mkdirSync(cwd)
      execSync('cd ' + cwd)
      execSync('npm link macron')
    } catch (err) {
      if (err.code !== 'EEXIST') throw err
    }
  } else {
    appName = basename(cwd)
    // cwd = cwd + appName + pathSeperator
    execSync('npm link macron')
  }

  const appConfigFilePath = cwd + 'macron.config.js'
  const indexHTMLFilePath = cwd + 'public/index.html'
  const packageJsonFilePath = cwd + 'package.json'
  const licenseFilePath = cwd + 'LICENSE'
  const gitIgnoreFilePath = cwd + '.gitignore'
  const npmIgnoreFilePath = cwd + '.npmignore'

  // Macron configuration file
  if (existsSync(appConfigFilePath)) {
    process.stdout.write(
      chalk.hex('#ffa500')('\n    This project is already a macron app.\n\n')
      + '    Run: ' + chalk.cyan('macron start\n\n')
    )
    process.exit(0)
  }
  
  writeFileSync(
    appConfigFilePath,
    require('./temps/macron-config')(appName)
  )

  if (!existsSync(cwd + 'public')) {
    mkdirSync(cwd + 'public')
    
    if (!existsSync(cwd + 'public/icons'))
      mkdirSync(cwd + 'public/icons')
  }
  
  // App root HTML file
  if (!existsSync(indexHTMLFilePath))
    writeFileSync(
      indexHTMLFilePath,
      require('./temps/index-html')
    )

  // Copy icon.ico to project
  createReadStream(normalize(__dirname + '/temps/icon.ico')).pipe(
    createWriteStream(cwd + 'public/icons/icon.ico')
  )
  
  // package.json file
  if (!existsSync(packageJsonFilePath))
    writeFileSync(
      packageJsonFilePath,
      require('./temps/package-json')(appName)
    )

  // package.json file
  if (!existsSync(licenseFilePath))
    writeFileSync(
      licenseFilePath,
      require('./temps/package-json')(appName)
    )

  // gitignore file
  if (!existsSync(gitIgnoreFilePath))
    writeFileSync(
      gitIgnoreFilePath,
      require('./temps/gitignore')
    )

  // gitignore file
  if (!existsSync(npmIgnoreFilePath))
    writeFileSync(
      npmIgnoreFilePath,
      require('./temps/gitignore')
    )

  process.stdout.write(
    `\n    ${appName + chalk.green(' created successfully.')}\n    Run: ${chalk.cyan('cd '+appName)}\n\n`
  )
}