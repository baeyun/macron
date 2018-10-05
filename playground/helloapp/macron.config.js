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
// .on('activate', function() {
//   alert("Welcome to Macron\'s \'Hello, World!\' App")
// })
// .on('close', function() {
//   alert('App is being closed.')
// })

module.exports = {
  name: 'HelloApp',
  mainWindow: App,
  build: {
    buildPath: './build',
    distributionPath: './dist',
    autoGenerateIconSizes: true,
    debugMode: false
  }
}
