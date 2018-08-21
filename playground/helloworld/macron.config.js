/**
 * Macron Configuration File
 */
// const { Window } = require('macron')

// Macron.Window API
var MacronRegisteredWindows = {}
var MacronRegisteredEventCallbacks = {close: []}
const { sep: pathSeperator } = require('path')
const cwd = process.cwd() + pathSeperator
const Window = function(config={}) {
  // Register window
  this.UID = Object.keys(MacronRegisteredWindows).length + 1
  MacronRegisteredWindows[this.UID] = this

  let {
    title = 'Macron App',
    height = 500,
    width = 500,
    maxHeight = null,
    maxWidth = null,
    minHeight = null,
    minWidth = null,
    resizable = true,
    focusOnStartup = true,
    hideInTaskbar = false,
    hideOnStartup = false,
    startupFromCenter = false,
    startupState = "normal",
    frameless = false,

    devServerURI = null,
    sourcePath = null,
    nativeDependencies = null
  } = config
  
  this.title = title
  this.height = height
  this.width = width
  if (maxHeight) this.maxHeight = maxHeight
  if (maxWidth) this.maxWidth = maxWidth
  if (minHeight) this.minHeight = minHeight
  if (minWidth) this.minWidth = minWidth
  this.resizable = resizable
  this.focusOnStartup = focusOnStartup
  this.hideInTaskbar = hideInTaskbar
  this.hideOnStartup = hideOnStartup
  this.startupFromCenter = startupFromCenter
  this.startupState = startupState
  this.frameless = frameless
  
  this.rootPath = cwd
  if (devServerURI) this.devServerURI = devServerURI
  this.sourcePath = sourcePath.replace("./", "").replace(/[/|\\]/g, pathSeperator)
  this.nativeDependencies = nativeDependencies

  // Window events
  this.on = function(eventType, callback) {
    MacronRegisteredEventCallbacks[eventType].push(callback)
    
    return this
  }

  return this
}

const App = new Window({
  title: "Sample App",
  height: 960,
  width: 1500,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  // frameless: true,
  // startupState: "maximized",
  // devServerURI: 'http://127.0.0.1:8888/browser-script-editor/',
  sourcePath: './public/index.html',
  // menu: require('./src/main-app-menubar'),
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})
// .on('close', function() {
//   console.log('App is closed')
// })
// .on('close', function() {
//   console.log('Another callback on the close event')
// })

// for(let event in MacronRegisteredEventCallbacks) {
//   MacronRegisteredEventCallbacks[event].forEach(e => {
//     e.call()
//   });
// }

module.exports = {
  name: 'Hello World App',
  mainWindow: App,
  // devServerURI: 'http://127.0.0.1:8888',
  nativeScriptsPath: './native/',
  iconSource: './src/img/icon.png',
  // icons: [
  //   './src/img/icon_x32.ico',
  //   './src/img/icon_x64.ico',
  //   './src/img/icon_x150.ico'
  // ],
  autoGenerateIconSizes: true,
  buildPath: './builds'
}
