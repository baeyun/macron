#!/usr/bin/env node

// prompts required build tools
// require('./dependencyChecks')()

const { version } = require('../package.json')
const { sep: pathSeperator } = require('path')
const chalk = require('chalk')

const cwd = process.cwd() + pathSeperator
const [,, ...args] = process.argv

switch(args[0]) {
  /**
   * macron init example-app
   */
  case 'init':
    require('./init')(cwd, args[1] || null)
    break
  
  /**
   * macron start
   */
  case 'start':
    require('./start')(cwd, args[1] || null)
    break

  /**
   * macron generate-icons
   */
  case 'generate-icons':
    require('./generate-icons')(cwd)
    break

  /**
   * macron build
   */
  case 'build':
    require('./build')(cwd)
    break

  /**
   * macron deploy
   */
  case 'deploy':
    require('./deploy')(cwd)
    break

  /**
   * macron version
   */
  case '--version':
  case 'version':
  case '-v':
    console.log('\n  Macron Version: ' + chalk.hex('#ffa500')(version) + '\n')
    break
  
  /**
   * macron version
   */
  case '--help':
  case 'help':
  case '-h':
  default:
    console.log(`
  Welcome to Macron ${chalk.grey('- Version: ' + version)}

    Command usage: ${chalk.hex('#ffa500')('macron')} <command>
  
  AVAILABLE COMMANDS:
    
    ${chalk.hex('#ffa500')('init')}
      Creates a Macron project: ${chalk.hex('#ffa500')('macron')} init <projectName>. If no project
      name is provided, it uses the directory name where it is run as the
      project name.
      This command could also be use to transform existing projects into
      Macron projects by simply running: macron init in the projects folder.

    ${chalk.hex('#ffa500')('start')}
      Runs the ${chalk.grey("'./public/index.html'")} in a temporary / non-build Macron app.
      This is useful for development.

    ${chalk.hex('#ffa500')('build')}
      Creates a build of the Macron projects ${chalk.grey("'./public/'")} directory.

    ${chalk.hex('#ffa500')('deploy')}
      Creates a setup wizard for the project and places it in the ${chalk.grey("'./public/'")}
      directory. It then builds and archives the macron project into zip form.
      The setup wizard is configured to download this zip archive as additional
      app files during the installation process on the clients computer. It
      gets the latest build version by checking a ${chalk.grey("'.version'")} file
      in the Macron project's root directory.

    ${chalk.hex('#ffa500')('--version | version | -v')}
      These commands simply return the current version of Macron that you are
      running

    ${chalk.hex('#ffa500')('--help | help | -h')}
      These commands couple with the ${chalk.hex('#ffa500')('macron')} command produce brief
      documentation on all available Macron commands. For more info, visit our
      online documention pages via: ${chalk.grey('http://macron.io/docs')}
    `)
    break
}

