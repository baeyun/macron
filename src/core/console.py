import os
import sys
import chalk
import webview
from pathlib import Path

from fs import FileSystem

class Console:
  def __init__(self, app_root_path):
    # Create logfile
    self.logfile_stream = self.init_logfile(app_root_path)
    self.fs = FileSystem()

  def init_logfile(self, app_root_path):
    logfile_path = Path(app_root_path + "newtron-debug.log")

    if logfile_path.is_file():
      f = open(logfile_path, "a")
      f.truncate(0)
      return f

    return open(logfile_path, "a")
  
  def close_stream(self):
    # @todo Close self.logfile_stream
    self.logfile_stream.close()

  def log(self, params):
    # Convert webview-generated tuples to strings before writing
    self.logfile_stream.write(''.join(params["toLog"]))
    self.fs.sync_file_updates(self.logfile_stream)
  
  def clear(self):
    self.logfile_stream.truncate(0)
    self.logfile_stream.write('\x1bc')
    self.fs.sync_file_updates(self.logfile_stream)