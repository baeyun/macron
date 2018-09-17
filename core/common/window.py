from macron import *

import platform
import sys
from os import path

dirname = path.dirname(path.realpath(__file__))

if platform.system() == "Windows":
  sys.path.append(path.join(dirname, '../windows/'))
elif platform.system() == "Linux":
  sys.path.append(path.join(dirname, '../linux/'))

from window import MacronWindow

class Window(NativeBridge):
  @macronMethod
  def create(self, config):
    win = MacronWindow(config)
    # win.Owner = self.window
    win.show()
    