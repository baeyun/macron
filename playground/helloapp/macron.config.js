/**
 * Macron Configuration File
 */
const { Window } = require('../../index') // require('macron')

const App = new Window({
  title: "Sample App",
  height: 960,
  width: 1500,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  // frameless: true,
  // startupState: "maximized",
  // devServerURI: 'http://whatismybrowser.com/',
  sourcePath: './public/index.html',
  nativeModules: ['hello.py']
  // menu: require('./src/main-app-menubar'),
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})
// .on('close', function() {
//   console.log('App is closed')
// })
// .on('close', function() {
//   console.log('Another callback on the close event')
// })

module.exports = {
 name: 'Hello World App',
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
