#!/usr/bin/env node

// prompts required build tools
// require('./dependencyChecks')()

const { sep: pathSeperator } = require('path')

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
    require('./start')(cwd, args[1] == 'build')
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
}

