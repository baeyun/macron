from macron import NativeBridge

import platform

class System(NativeBridge):
  def platform(self):
    return platform.platform()

  def system(self):
    return platform.version()
  
  def machine(self):
    return platform.machine()
    
  def node(self):
    return platform.node()
  
  def processor(self):
    return platform.processor()
  
  def release(self):
    return platform.release()
  
  # def system_alias(self):
  #   return platform.system_alias()
  
  def uname(self):
    return str(platform.uname()) # @expect to return JavaScript array
  
  # Java Platform
  def java_ver(self):
    return str(platform.java_ver()) # @expect to return JavaScript array
  
  # Win32 Platform
  def win32_ver(self):
    return str(platform.win32_ver()) # @expect to return JavaScript array
  
  # Win95/98 Platform. Deprecated since version 3.3
  # We are downgrading to version 2.7 anyways.
  # def popen(self):
  #   return platform.popen()
  
  # Mac OS Platform
  # A single unified check exists (System.system()) i.e. If you run
  #     if (System.getPlatform() == "MacOSX") {
  #       if (System.macVersion() == "Sierra High") {
  #         // Run MacOS-specific commands
  #       }
  #     }
  def mac_ver(self):
    return str(platform.mac_ver()) # 
  
  # Unix Platforms
  # Deprecated since version 3.5, will be removed in version 3.7
  def dist(self):
    return str(platform.dist()) # Alias for linux_distribution. @expect to return JavaScript array
  
  def libc_ver(self):
    return str(platform.libc_ver()) # @expect to return JavaScript array