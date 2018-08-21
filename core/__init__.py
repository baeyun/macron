import sys
import os
from json import loads

# Get current dir
dirname = os.path.dirname(os.path.realpath(__file__))

"""
Not only must the imports be done inside functions
(thank God it works in Python), the code piece:

sys.path.append(os.path.join(dirname, <OS_NAME>))

must also be included just before the respective OS's
native API is imported. This is because no module should
block the main thread since modules like 'clr' aren't
available in Linux (i.e. Windows-only).

For instance:
  if os is 'windows':
    sys.path.append(os.path.join(dirname, 'windows'))
    # Not necessary to name import since check is already done!
    from window import create_window as create_windows_mswin
"""

# sys.path.append(os.path.join(dirname, 'windows'))
sys.path.append(os.path.join(dirname, 'linux'))

# from core import MacronCoreAPI
# from window import create_window as create_windows_mswin
from window import create_window as create_windows_linux

def get_os():
  return

def main(args):
  app_config = loads(loads(args[1]))
  # app_root_path = app_config["appRootPath"].replace("//", "\u005c")
  # app_html_path = app_config["sourcePath"]
  # app_dev_uri = app_config["devServerURI"]
  
  # @todo handle err
  if "mainWindow" not in app_config:
    print("Error: 'mainWindow' property not defined in macron.config.js")

  create_windows_linux(config=app_config["mainWindow"])

if __name__ == "__main__":
  main(args=sys.argv)
