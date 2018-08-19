/**
 * Macron Configuration File
 */
const { Window } = require('macron')

const MainView = new Window({
  title: 'Hello World App',
  sourcePath: './public/index.html',
  nativeDependencies: ['numpy.py']
})

const AuthView = new Window({
  title: 'Login',
  sourcePath: './public/login.html',
  nativeDependencies: [
    'auth.py',
    'oauth.py',
    'fbauthsdk.py',
    'Microsoft.x32.NET_SDK.dll'
  ]
})

// AuthView.on('close', function() {
//   console.log('AuthView closed')
// })

module.exports = {
  mainWindow: IsLoggedIn ? MainView : AuthView,
  devServerURI: 'https://mail.google.com',
  nativeScriptsPath: './native/',
  logoPath: './src/img/logo.png',
  autoGenerateLogoSizes: true,
  buildPath: './builds'
}
