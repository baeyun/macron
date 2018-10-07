"""
The Archive module currently supports zipfile-related functionalities.
Several archive extensions are in mind e.g. .rar, .gzip using zlib.
For encrypted archives (encrypted bytes, not regular passwords), check the
crypto module.
"""

from macron import *

from zipfile import ZipFile

class Archive(NativeBridge):
  # @todo Resolve relative paths
  @macronMethod
  def writeZip(self, zipname, files):
    with ZipFile(zipname, 'w') as zipf:
      for f in files:
        # Could be existing files
        zipf.write(f)
  
  # @todo Enhance compatibility with HTML (UTF-8)
  @macronMethod
  def readZip(self, zipname, file):
    with ZipFile(zipname) as zipf:
      with zipf.open(file) as f:
          return str(f.read())
  
  # Warning: This should not be available for disclosure
  # @todo Convert str to bytes for pwd
  @macronMethod
  def setPassword(self, zipname, pwd=None):
    ZipFile(zipname).setpassword(bytes(pwd))
    return
  
  @macronMethod
  def extractMember(self, zipname, member=None, extraction_path="/"):
    ZipFile(zipname).extract(member, path=extraction_path)
    return
  
  @macronMethod
  def extractAll(self, zipname, extraction_path="/"):
    ZipFile(zipname).extractall(extraction_path)
    return
  
  # @todo Convert ZipInfo class to JavaScript object
  @macronMethod
  def getinfo(self, zipname, key):
    # return ZipFile(zipname).getinfo(key)
    # Return ZIP name for now
    return ZipFile(zipname).filename
  
  # @todo Get zip size
  @macronMethod
  def getSize(self, zipname):
    return ZipFile(zipname).file_size
  
  @macronMethod
  def getChildren(self, zipname):
    return ZipFile(zipname).namelist().__str__()