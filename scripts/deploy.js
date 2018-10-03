const { existsSync, writeFileSync } = require('fs')
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
  
  const setupDefaultSettings = {
    'install_path': null,
    'create_shortcut': true,
    'start_after_setup': true,
    'app_name': 'MacronApp',
    'setup_banner': 'setup-banner.png',
    'setup_logo': 'vue.png',
    'app_license': 'MIT License',
    'build_info_src': 'http://localhost:3000/releases/app/.setupinfo'
  }

  const qualifiedAppName = appConfig.name.replace(/\s/g, '_')
  const spinner = ora('Starting deployment process...').start()

  const buildProcess = exec([
    `pyinstaller`,
    `--name=${qualifiedAppName}Setup`,
    `--icon=${cwd}app/assets/icon.ico`,
    `--workpath=app`,
    `--distpath=dist`,
    `--specpath=app`,
    `--hiddenimport=tkinter`,
    `--hiddenimport=tkinter.messagebox`,
    `--hiddenimport=tkinter.filedialog`,
    `--hiddenimport=pygubu`,
    `--hiddenimport=pygubu.builder.ttkstdwidgets`,
    // `--hiddenimport=PIL.ImageTk`,
    // `--hiddenimport=PIL.Image`,
    // `--hiddenimport=json`,
    `--add-data=assets;assets`,
    // '--log-level DEBUG',
    '-F',
    // '-c',
    '-w',
    '-y',
    'app/__wizard__.py'
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
    // writeFileSync(
    //   `${cwd}build/${qualifiedAppName}Setup/.setupinfo`,
    //   JSON.stringify(setupDefaultSettings),
    //   'utf8'
    // )

    spinner.stop()
    process.stdout.write(
      chalk.green('\n    Setup wizard built successfully.\n')
    )
  })
}
