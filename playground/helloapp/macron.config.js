/**
 * Macron Configuration File
 */
const { Window } = require('../../index') // require('macron')

const App = new Window({
  title: "MacLine",
  width: 1200,
  height: 960,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  // frameless: true,
  // startupState: "maximized",
  // devServerURI: 'http://localhost:3000/',
  sourcePath: './public/index.html',
  // nativeModules: ['Dialog'],
  menu: require('./src/menubar'),
  // accelerators: require('./src/keybindings'),
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})
// .on('activate', function() {
//   alert("Welcome to Macron\'s \'Hello, World!\' App")
// })
// .on('close', function() {
//   alert('App is being closed.')
// })

module.exports = {
  name: 'TestApp',
  mainWindow: App,
  nativeModulesPath: './native/',
  iconSource: './src/img/icon.png',
  autoGenerateIconSizes: true,
  buildPath: './builds'
}
