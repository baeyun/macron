const { existsSync, writeFileSync } = require('fs')
const { sep: pathSeperator, normalize } = require('path')
const { exec } = require('child_process')
const chalk = require('chalk')
const ora = require('ora')

module.exports = function(cwd) {
  const appConfigFilePath = cwd + 'macron.config.js'
  const appConfig = require(appConfigFilePath)
  
  if (!existsSync(appConfigFilePath))
    throw new Error('MACRON ERR: Application must include a macron.config.js config file.')
  
  if (!appConfig.name)
    throw new Error('MACRON ERR: macron.config.js must include a name property.')
  
  appConfig.cwd = cwd
  appConfig.mainWindow.nativeModulesPath = appConfig.nativeModulesPath.replace("./", "").replace(/[/|\\]/g, pathSeperator)
  
  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')
  const spinner = ora('Starting build process...').start()

  writeFileSync(
    `${cwd}/.builddata`,
    JSON.stringify(appConfig),
    'utf8'
  )

  const buildProcess = exec([
    'pyinstaller',
    `--name=${qualifiedAppName}`,
    `--icon=${cwd}public/assets/icon.ico`,
    `--workpath=` + normalize(__dirname + '/../cache'),
    `--distpath=${cwd}build`,
    `--specpath=` + normalize(__dirname + '/../core'),
    `--hiddenimport=clr`,
    `--hiddenimport=pathlib`,
    `--hiddenimport=json`,
    `--paths=${normalize(__dirname + '/../core')};${normalize(__dirname + '/../core/common')};${normalize(__dirname + '/../core/windows')}`,
    `--hiddenimport=_contextmenu`,
    `--hiddenimport=archive`,
    `--hiddenimport=currentwindow`,
    `--hiddenimport=windowmanager`,
    `--hiddenimport=fs`,
    `--hiddenimport=system`,
    // `--add-binary=` + normalize(__dirname + '/../core/windows/assemblies/MacronWebviewInterop.dll'), // Windows specific
    `--add-data=${normalize(__dirname + '/../core/windows/assemblies/MacronWebviewInterop.dll')};assemblies`, // Windows specific
    `--add-data=${cwd}/.builddata;.`,
    `--add-data=${cwd}public/assets/icon.ico;assets`,
    `--add-data=${normalize(__dirname + '/../src')};macron`,
    '--log-level DEBUG',
    '-c',
    // '-w',
    '-y',
    normalize(__dirname + '/../core/') + '__init__.py'
  ].join(' '), (err, stdout, stderr) => {
    if (err) {
      console.error(err)
      return
    }

    console.log(stdout)
  })

  buildProcess.stdout.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildProcess.stderr.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildProcess.on('exit', function(data) {
    spinner.stop()

    process.stdout.write(
      chalk.green('\n    Build process complete.\n')
      + '\n    Run: ' + chalk.cyan('macron start build') + ' to execute your app.\n'
    )
  })
}
