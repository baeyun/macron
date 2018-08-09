import sys
from os import getcwd
from json import loads
import webview

def main(args):
  app_config_path = args[1]
  app_config = loads(open(app_config_path + "newtron.config.json", 'r').read())

  uid = webview.create_window(app_config["name"], app_config_path + app_config["src"])

if __name__ == "__main__":
  main(args = sys.argv)
