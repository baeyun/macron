"""
This module defines all file-related functionalities included in the Macron
application system. Please refer to the official documentation site for more
details on this section.
"""

from macron import *

import os
import sys
import fnmatch
from pathlib import Path
from shutil import copyfile, rmtree

class FileSystem(NativeBridge): 
  
  # Saves immediately without waiting for close
  # Ensures file is synced with latest changes
  @macronMethod
  def syncFileUpdates(self, file_stream):
    file_stream.flush()
    os.fsync(file_stream.fileno())

  @macronMethod
  def writeFile(self, file_path, file_contents):
    f = open(file_path, "x")
    f.write(file_contents)
    # Make sure latest updates of file are synced with main thread
    self.sync_file_updates(f)
    f.close()

    """
    I'm not going to return the file object for now since the WebView context
    complains of converting Python objects/classes to JavaScript. This could also be great
    since the user will not interact with a lot of Python, which keeps us under the shadows.
    """
    # return f
  
  @macronMethod
  def readFile(self, file_path):
    with open(file_path, "r") as f:
      return f.read()
  
  @macronMethod
  def appendFile(self, file_path, file_contents):
    with open(file_path, "a") as f:
      f.write(file_contents)
      self.sync_file_updates(f)
      # return f.read()
  
  @macronMethod
  def clearFile(self, file_path):    
    with open(file_path, "w") as f:
      try:
        f.truncate(0)
        self.sync_file_updates(f)
        return True
      except Exception as e:
        return False
  
  @macronMethod
  def copyFile(self, src, to):
    # @note 'from' is a reserved keyword in Python

    """
    Use this to copy a full file path content to another
    file path. Use [shutil.copy()] to copy from a file to
    another dir.
    """
    copyfile(src, to)
    # return
  
  @macronMethod
  def isFile(self, file_path):
    return Path(file_path).is_file()
  
  @macronMethod
  def isDir(self, file_path):
    return Path(file_path).is_dir()
  
  @macronMethod
  def mkdir(self, file_path):
    if not self.is_dir(file_path):
      try:
        os.makedirs(file_path)
        return True
      except OSError as e:
        return False
  
  # Might not work while running in the same UI thread.
  # I think all common APIs should run in their own thread.
  @macronMethod
  def chdir(self, file_path):
    if not self.is_dir(file_path):
      try:
        os.chdir(file_path)
        return True
      except OSError as e:
        return False
  
  # Fixed!
  # Returns real path
  @macronMethod
  def realpath(self, file_path):
    file_path = Path(file_path)

    if file_path.exists():
      return str(file_path.resolve())
    return None
  
  # @note should be noted that if the files
  # are not in the working directory you will
  # need the full path.
  @macronMethod
  def rename(self, oldname, newname):
    os.rename(oldname, newname)
    # return
  
  # @note removes file permanently
  # @todo create temporary unlink
  @macronMethod
  def unlink(self, file_path):
    if self.is_file(file_path):
      os.remove(file_path)
    return
  
  # @note removes dir and content
  @macronMethod
  def rmdir(self, path):
    if self.is_dir(path):
      rmtree(path)
    return

  # @note os.rmdir() on Windows removes directory
  # symbolic link even if the target dir isn't empty
  @macronMethod
  def rmdirEmpty(self, path):
    if self.is_dir(path):
      os.rmdir(path)
    return
  
  # @todo enhance accessability by creating types
  @macronMethod
  def readDir(self, file_path):
    if self.is_dir(file_path):
      # This is supposed to be a JavaScript array but the bridge has
      # issues with converting types. I might find a solution to this
      # by using C++ to generate real JavaScript arrays, objects &/ other
      # interfaces. This means a user can:
      #     const { myFile } = fs.unlink('someFile.ts')
      #     fs.createFile(myFile.pathname)
      return str(os.listdir(file_path))
    return
  
  # @note unlike read_dir it returns a list with absolute
  # paths of files and dirs with Path(path)
  @macronMethod
  def readDirGlob(self, file_path, pattern):
    ff = []

    if self.is_dir(file_path):
      for f in os.listdir(file_path): # Could use self.read_dir() but there is a type issue
        if fnmatch.fnmatch(f, pattern):
          ff.append(f)

    return str(ff)
