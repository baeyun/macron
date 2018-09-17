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

# track windows
registered_windows = []

class Window(NativeBridge):
  
  @macronMethod
  def create(self, config):
    # create window
    window = MacronWindow(config)
    
    # register
    window.config['ID'] = len(registered_windows) + 1
    registered_windows.append(window)

    # TODO handle window ownership
    # window.Owner = self.window
    
    return window.config['ID']

  # TODO test
  @macronMethod
  def close(self, ID):
    if not registered_windows[ID]:
      return False

    registered_windows[ID].close()
    return True
  
  # TODO test
  @macronMethod
  def closeAll(self):
    if len(registered_windows) < 1:
      return False
    
    for window in registered_windows:
      window.close()
