const chalk = require('chalk')
const { spawnSync } = require('child_process')
const compareVersions = require('compare-versions')

module.exports = function() {
  /**
   * Python version check
   */
  let rawPythonVersion = spawnSync('python', ['--version']).output,
    pythonVersion = rawPythonVersion ? rawPythonVersion.toString().match(/\d\.\d\.\d/g)[0] : '0'

  // if (compareVersions(pythonVersion, '3.6.5') < 0)
  //   throw new Error(chalk.red('MACRON ERR: Macron requires Python version >= 3.6.5'))

  /**
   * Platform specific requirements
   */
  let dependencyStatus = []
  switch(process.platform) {
    case 'linux':
      ['python-gi', 'gir1.2-webkit-3.0'].map(function(dep, i) {
        let rawDepCheck = spawnSync('dpkg', ['-s', dep]).output.toString().includes('Status: install ok installed')
        dependencyStatus[i] = '        ' + chalk.cyan(dep)
        dependencyStatus[i] += ` ${chalk.grey('.').repeat(30 - dep.length)} ` // dots
        dependencyStatus[i] += rawDepCheck
          ? chalk.green('INSTALLED')
          : chalk.red('MISSING')
      })
      
      break
    case 'darwin':
      // let platformSpecificDeps = ['pyobjc']
      break
    case 'win32':
      // let platformSpecificDeps = ['pythonnet']
      break
  }

  process.stdout.write(
    [
      '\n    ',
      chalk.red('Macron requires the following dependencies:\n\n'),
      dependencyStatus.join('\n'),
      '\n\n\n'
    ].join('')
  )
}