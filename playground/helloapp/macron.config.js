/**
 * Macron Configuration File
 */
const { Window } = require('../../index') // require('macron')

const App = new Window({
  title: "HelloApp | Macron Test App",
  width: 1200,
  height: 960,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  // frameless: true,
  startupState: "maximized",
  devServerURI: 'animejs.com',
  sourcePath: './public/index.html',
  // nativeModules: ['Dialog'],
  menu: require('./src/menubar'),
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})
// .on('activate', function() {
//   alert("Welcome to Macron\'s \'Hello, World!\' App")
// })
// .on('close', function() {
//   alert('App is being closed.')
// })

module.exports = {
 name: 'Hello World App',
 mainWindow: App,
 nativeModulesPath: './native/',
 iconSource: './src/img/icon.png',
 // icons: [
 //   './src/img/icon_x32.ico',
 //   './src/img/icon_x64.ico',
 //   './src/img/icon_x150.ico'
 // ],
 autoGenerateIconSizes: true,
 buildPath: './builds'
}
