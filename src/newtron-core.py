import sys
from os import getcwd
from json import loads

def main(args):
  app_config_path = args[1]
  app_config = loads(open(app_config_path, 'r').read())

  print(app_config)

if __name__ == "__main__":
  main(args = sys.argv)
