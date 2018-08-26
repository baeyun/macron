from macron import NativeBridge

from platform import platform, system, version

class System(NativeBridge):
  def get_platform(self):
    return platform()

  def get_system(self):
    return version()
