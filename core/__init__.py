import sys
import os
from json import loads
import platform

# Get current dir for loading core components
dirname = os.path.dirname(os.path.realpath(__file__))

def main(args):
  app_config = loads(loads(args[1]))

  # @todo handle err
  if "mainWindow" not in app_config:
    print("Error: 'mainWindow' property not defined in macron.config.js")
  
  if platform.system() == "Windows":
    sys.path.append(os.path.join(dirname, 'windows'))
  elif platform.system() == "Linux":
    sys.path.append(os.path.join(dirname, 'linux'))
  
  from window import create_window
  create_window(config=app_config["mainWindow"])


if __name__ == "__main__":
  main(args=sys.argv)
