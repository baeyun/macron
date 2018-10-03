import sys
from os import path

# load macron core
# TODO load from 'npm root -g
MACRON_WIZARD_PATH = path.realpath(
  'C:/Users/bukharim96/Desktop/Projects/macron/core/'
)
sys.path.append(MACRON_WIZARD_PATH)

from wizard import MacronSetupWizard

def main():
  MacronSetupWizard()

if __name__ == "__main__":
  main()
