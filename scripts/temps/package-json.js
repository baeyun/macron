const { version: macronVersion } = require('../../package.json')
const { sync: getCurrentUsername } = require('username')

module.exports = function(appName) {
return `{
  "name": "${appName}",
  "version": "0.1.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "macron start"
  },
  "author": "${getCurrentUsername() || ''}",
  "license": "MIT",
  "devDependencies": {
    "macron": "^${macronVersion}"
  }
}
`
}
