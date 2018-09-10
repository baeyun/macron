// requirejs polyfill

window.require = function(moduleName) {
  return window[moduleName]
}
