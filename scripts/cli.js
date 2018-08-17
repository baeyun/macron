#!/usr/bin/env node

// prompts required build tools
// require('./dependencyChecks')()

// const meow = require('meow');
const { normalize } = require('path')

const cwd = normalize(process.cwd() + '/')
const [,, ...args] = process.argv

switch(args[0]) {
  /**
   * macron init example-app
   */
  case 'init':
    require('./init')(cwd, args[1])
    break
  
  /**
   * macron start
   */
  case 'start':
    require('./start')(cwd)
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
}

