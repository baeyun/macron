/**
 * Macron Configuration File
 */
// const { Window } = require('macron')

var MacronRegisteredWindows = {}

var MacronRegisteredEventCallbacks = {
  close: []
}

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
  
  this.sourcePath = sourcePath
  this.nativeDependencies = nativeDependencies

  // Window events
  this.on = function(eventType, callback) {
    MacronRegisteredEventCallbacks[eventType].push(callback)
    
    return this
  }

  return this
}

const App = new Window({
  title: "Joker",
  height: 700,
  width: 900,
  minHeight: 500,
  minWidth: 500,
  startupFromCenter: true,
  frameless: true
  // menu: require('./src/main-app-menubar'),
  // sourcePath: './public/index.html',
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
  devServerURI: 'https://mail.google.com',
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
