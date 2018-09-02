/**
 * Macron APIs initializers
 */

var _Macron = {}

// All windows created during app lifespan
_Macron.RegisteredWindows = {}

// Triggered by native-end
_Macron.RegisteredEventCallbacks = {
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

// _Macron.invokeEventCallbacks = function(event) {
//   for(callback in _Macron.RegisteredEventCallbacks[event])
//     callback.call()
// }
