module.exports = function(appName) {
return `/**
* Macron Configuration File
*/

module.exports = {
  name: '${appName}',
  devServerURI: 'http://localhost:3000/',
  sourcePath: './public',
  // nativeScriptsPath: './native',
  // logoPath: './src/img/logo.png',
  // autoGenerateLogoSizes: true,
  buildPath: './builds'
}
`
}