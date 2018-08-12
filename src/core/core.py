import sys
from json import loads
import webview
import chalk
import threading

from console import Console
from fs import FileSystem
from window import Window

# from console.console import Console
# from fs.fs import FileSystem
# from window.window import Window

# import fs as FileSystem
# import console as Console
# import window as Window

class MacronCoreAPI:
  def __init__(self, app_root_path):
    self.console = Console(app_root_path)
    self.fs = FileSystem(console=self.console)
    self.window = None
  
  """ Core Native APIs """

  # Console API
  def log(self, params):
    self.console.log(params)
  
  def clear(self, params):
    self.console.clear()
  
  # File API
  def open_file_dialog(self, params):
    return self.fs.open_file_dialog(params)
  
  def write_file(self, params):
    self.fs.write_file(params)
  
  def read_file(self, params):
    return self.fs.read_file(params)
  
  def append_file(self, params):
    return self.fs.append_file(params)
  
  def clear_file(self, params):
    return self.fs.clear(params)
  
  def copy_file(self, params):
    return self.fs.copy_file(params)
  
  def is_file(self, params):
    return self.fs.is_file(params)
  
  def is_directory(self, params):
    return self.fs.is_dir(params)
  
  def mkdir(self, params):
    return self.fs.mkdir(params)
  
  def chdir(self, params):
    return self.fs.chdir(params)
  
  def realpath(self, params):
    return self.fs.realpath(params)
  
  def rename_file(self, params):
    return self.fs.rename(params)
  
  def unlink(self, params):
    return self.fs.unlink(params)
  
  def rmdir(self, params):
    return self.fs.rmdir(params)
  
  def rmdir_empty(self, params):
    return self.fs.rmdir_empty(params)
  
  def read_dir(self, params):
    return self.fs.read_dir(params)
  
  def read_dir_glob(self, params):
    return self.fs.read_dir_glob(params)

  # Window API
  def create_window(self, config):
    self.window = Window().create(config)

    # self.fs.inject_js({
    #   "script": "alert('Hello. I am a modal from Python!')"
    # })
  
  def close_window(self, params):
    self.window.close()
  
  def quit_application(self, params):
    self.console.close_stream()
    self.window.quit()
