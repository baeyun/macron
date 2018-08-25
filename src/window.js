// Macron.Window API
var MacronRegisteredWindows = {}
var MacronRegisteredEventCallbacks = {close: []}

// for(let event in MacronRegisteredEventCallbacks) {
//   MacronRegisteredEventCallbacks[event].forEach(e => {
//     e.call()
//   });
// }

const { sep: pathSeperator } = require('path')
const cwd = process.cwd() + pathSeperator

module.exports = function(config={}) {
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
    nativeModules = [],
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
  this.nativeModules = nativeModules.map(
    path => path.replace("./", "").replace(/[/|\\]/g, pathSeperator)
  )
  this.nativeDependencies = nativeDependencies

  // Window events
  this.on = function(eventType, callback) {
    MacronRegisteredEventCallbacks[eventType].push(callback)
    
    return this
  }

  return this
}
