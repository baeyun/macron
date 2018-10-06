module.exports = function(appName) {
return `/**
* Macron Configuration File
*/
const { Window } = require('macron')

const App = new Window({
  title: '${appName} App',
  width: 1200,
  height: 960,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  // menu: require('./src/menubar'),
  // devServerURI: 'http://localhost:3000/', // no effect on build
})

module.exports = {
  appName: '${appName}',
  mainWindow: App,
  build: {
    debugMode: false
  }
}
`
}