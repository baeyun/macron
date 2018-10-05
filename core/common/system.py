# TODO: Python modules do not return a corresponding JavaScript value for different data types

from macron import *

import platform

class System(NativeBridge):
  @macronMethod
  def getPlatform(self):
    return platform.platform()

  @macronMethod
  def getSystem(self):
    return platform.version()
  
  @macronMethod
  def getMachine(self):
    return platform.machine()
    
  @macronMethod
  def getNetworkName(self):
    return platform.node()
  
  @macronMethod
  def getProcessor(self):
    return platform.processor()
  
  @macronMethod
  def getRelease(self):
    return platform.release()
  
  # @macronMethod
  # def system_alias(self):
  #   return platform.system_alias()
  
  @macronMethod
  def uname(self):
    return str(platform.uname()) # @expect to return JavaScript array
  
  # Java Platform
  @macronMethod
  def getJavaVersion(self):
    return str(platform.java_ver()) # @expect to return JavaScript array
  
  # Win32 Platform
  @macronMethod
  def win32Version(self):
    return str(platform.win32_ver()) # @expect to return JavaScript array
  
  # Win95/98 Platform. Deprecated since version 3.3
  # We are downgrading to version 2.7 anyways.
  # @macronMethod
  # def popen(self):
  #   return platform.popen()
  
  # Mac OS Platform
  # A single unified check exists (System.system()) i.e. If you run
  #     if (System.getPlatform() == "MacOSX") {
  #       if (System.macVersion() == "Sierra High") {
  #         // Run MacOS-specific commands
  #       }
  #     }
  @macronMethod
  def macVersion(self):
    return str(platform.mac_ver()) # 
  
  # Unix Platforms
  # Deprecated since version 3.5, will be removed in version 3.7
  @macronMethod
  def getLinuxDistribution(self):
    return str(platform.dist()) # Alias for linux_distribution. @expect to return JavaScript array
  
  @macronMethod
  def libcVersion(self):
    return str(platform.libc_ver()) # @expect to return JavaScript array