"""
The Archive module currently supports zipfile-related functionalities.
Several archive extensions are in mind e.g. .rar, .gzip using zlib.
For encrypted archives (encrypted bytes, not regular passwords), check the
crypto module.
"""

from macron import NativeBridge

from zipfile import ZipFile, ZIP64_LIMIT, ZIP64_VERSION, ZIP_FILECOUNT_LIMIT, ZIP_FILECOUNT_LIMIT, ZIP_BZIP2, ZIP_DEFLATED, ZIP_LZMA, ZIP_MAX_COMMENT, ZIP_STORED

class Archive(NativeBridge):
  # @todo Resolve relative paths
  def write_zip(self, zipname, files):
    with ZipFile(zipname, 'w') as zipf:
      for f in files:
        # Could be existing files
        zipf.write(f)
  
  # @todo Enhance compatibility with HTML (UTF-8)
  def read_zip(self, zipname, file):
    with ZipFile(zipname) as zipf:
      with zipf.open(file) as f:
          return str(f.read())
  
  # Warning: This should not be available for disclosure
  # @todo Convert str to bytes for pwd
  def set_password(self, zipname, pwd=None):
    ZipFile(zipname).setpassword(bytes(pwd))
    return
  
  def extract_member(self, zipname, member=None, extraction_path="/"):
    ZipFile(zipname).extract(member, path=extraction_path)
    return
  
  def extract_all(self, zipname, extraction_path="/"):
    ZipFile(zipname).extractall(extraction_path)
    return
  
  # @todo Convert ZipInfo class to JavaScript object
  def getinfo(self, zipname, key):
    # return ZipFile(zipname).getinfo(key)
    # Return ZIP name for now
    return ZipFile(zipname).filename
  
  # @todo Get zip size
  def get_size(self, zipname):
    return ZipFile(zipname).file_size
  
  def get_children(self, zipname):
    return ZipFile(zipname).namelist().__str__()