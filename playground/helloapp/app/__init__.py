import sys
from os import path

# load macron core
# TODO load from 'npm root -g
MACRON_CORE_PATH = path.realpath(
  'C:/Users/bukharim96/Desktop/Projects/macron/'
)
sys.path.append(MACRON_CORE_PATH)

from core import MacronApp

def main(argv):
  MacronApp(argv)

if __name__ == "__main__":
  main(argv=sys.argv)
