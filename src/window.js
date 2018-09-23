// macron.Window API

const { sep: pathSeperator } = require('path')
const cwd = process.cwd() + pathSeperator

var _Macron = {}

module.exports = function(config={}) {
  // Register window
  if (_Macron.RegisteredWindows) {
    this.UID = Object.keys(_Macron.RegisteredWindows).length + 1
    _Macron.RegisteredWindows[this.UID] = this
  }

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
    menu = null,
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
  this.menu = menu
  this.nativeDependencies = nativeDependencies

  // Window events
  this.eventCallbacks = {
    activate: [],
    close: [],
    closing: [],
    contextMenuClose: [],
    contextMenuOpen: [],
    deactivate: [],
    focusChange: [],
    keydown: [],
    keyup: [],
    sizeChange: [],
    stateChange: []
  }
  
  this.on = function(eventType, callback) {
    this.eventCallbacks[eventType].push(
      // double-quotes work-around
      callback.toString().replace(/\"/gi, "\'\'\'")
    )
    
    return this // Allow chaining
  }

  return this
}
