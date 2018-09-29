/**
 * Macron APIs initializers
 */

var _macron = {}

// All windows created during app lifespan
_macron.RegisteredWindows = {}

// Triggered by native-end
_macron.RegisteredEventCallbacks = {
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

// Menu events
_macron.registeredMenuCallbacks = []

// _macron.invokeEventCallbacks = function(event) {
//   for(callback in _macron.RegisteredEventCallbacks[event])
//     callback.call()
// }
