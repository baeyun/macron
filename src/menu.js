// macron.Menu Constants API

module.exports = {
  SEPERATOR: {seperator: true},
  callback: function(func) {
    return func.toString().replace(/\/\*[\s\S]*?\*\/|([^\\:]|^)\/\/.*$/gm, '')
  }
}