/**
 * Macron Configuration File
 */
const { Window } = require('../../index') // @todo require('macron')

const App = new Window({
  title: 'Macron HelloWorld App',
  width: 1200,
  height: 960,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  menu: require('./src/menubar'),
  // devServerURI: 'http://localhost:3000/', // only available during development
})

module.exports = {
  appName: 'HelloApp',
  mainWindow: App,
  build: {
    debugMode: false
  }
}
