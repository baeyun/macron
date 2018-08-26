import platform
from macron import NativeBridge

class System(NativeBridge):
  def get_platform(self):
    return platform.platform()
