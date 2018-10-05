import sys
from os import path
import platform
from json import load, loads

# Get current dir for loading core components
dirname = path.dirname(path.realpath(__file__))
sys.path.append(dirname)

if platform.system() == "Windows":
  sys.path.append(path.join(dirname, 'windows'))
elif platform.system() == "Linux":
  sys.path.append(path.join(dirname, 'linux'))

from window import create_window

class MacronApp:
  def __init__(self, argv):
    try:
      app_config = loads(loads(argv[1]))
      RESOURCE_PATH = app_config['cwd']
    except IndexError:
      RESOURCE_PATH = path.join(sys._MEIPASS, '')

      with open(RESOURCE_PATH + 'macron/.builddata') as f:
        app_config = load(f)
    
    # @todo handle err
    if "mainWindow" not in app_config:
      print("Error: 'mainWindow' property not defined in macron.config.js")
    
    create_window(config=app_config["mainWindow"])

if __name__ == "__main__":
  MacronApp(argv=sys.argv)
