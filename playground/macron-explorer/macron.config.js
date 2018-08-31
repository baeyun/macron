/**
 * Macron Configuration File
 */
const { Window } = require('../../index') // require('macron')

const App = new Window({
  title: "Macron Explorer",
  height: 600,
  width: 800,
  startupFromCenter: true,
  sourcePath: './src/index.html',
  nativeModules: [],
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})

module.exports = {
 name: 'Macron Explorer',
 mainWindow: App,
 // devServerURI: 'http://127.0.0.1:8888',
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
