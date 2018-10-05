const { existsSync, writeFileSync } = require('fs')
const { normalize } = require('path')
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

  if (!existsSync('./LICENSE'))
    throw new Error('MACRON ERR: A LICENSE file is required for deployment. Please include it in your project root.')

  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')
  const spinner = ora('Starting deployment process...').start()

  const setupInfo = {
    'app_name': appConfig.name
  }

  writeFileSync(
    `${cwd}/.setupdata`,
    JSON.stringify(setupInfo),
    'utf8'
  )

  const buildWizardProcess = exec([
    'pyinstaller',
    `--name=${qualifiedAppName}Setup`,
    `--icon=${cwd}public/assets/icon.ico`,
    `--workpath=` + normalize(__dirname + '/../cache'),
    // `--distpath=${cwd}dist`,
    `--specpath=` + normalize(__dirname + '/../cache'),
    `--hiddenimport=tkinter`,
    `--hiddenimport=tkinter.messagebox`,
    `--hiddenimport=tkinter.filedialog`,
    `--hiddenimport=json`,
    `--hiddenimport=urllib.request`,
    `--hiddenimport=pygubu`,
    `--hiddenimport=pygubu.builder.ttkstdwidgets`,
    // `--hiddenimport=PIL.ImageTk`,
    // `--hiddenimport=PIL.Image`,
    // `--hiddenimport=json`,
    `--add-data=${cwd}/.setupdata;.`,
    `--add-data=${normalize(__dirname + '/../')}core/wizard/views;assets/views`,
    `--add-data=${cwd}public/;assets/public`,
    `--add-data=${cwd}LICENSE;assets`,
    // '--log-level DEBUG',
    // '-c',
    '-F',
    '-w',
    '-y',
    normalize(__dirname + '/../core/wizard/') + '__wizard__.py'
  ].join(' '), (err, stdout, stderr) => {
    if (err) {
      console.error(err)
      return
    }
    
    console.log(stdout)
  })

  buildWizardProcess.stdout.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildWizardProcess.stderr.on('data', function(data) {
    spinner.text = data.toString()
  })

  buildWizardProcess.on('exit', function(data) {
    spinner.stop()
    process.stdout.write(
      chalk.green('\n    Setup wizard built successfully.\n')
      + '\n    Run: ' + chalk.cyan('macron start wizard') + ' to test your app\'s setup wizard.\n'
    )
  })
}
