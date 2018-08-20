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
    sourcePath = null,
    nativeDependencies = null
  } = config
  
  this.title = title
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
  // sourcePath: './public/index.html',
  // nativeDependencies: ['numpy.py', 'ffmpeg.py']
})
.on('close', function() {
  console.log('App is closed')
})
.on('close', function() {
  console.log('Another callback on the close event')
})

// for(let event in MacronRegisteredEventCallbacks) {
//   MacronRegisteredEventCallbacks[event].forEach(e => {
//     e.call()
//   });
// }

console.log({
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
})
