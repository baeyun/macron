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
    self.fs = FileSystem()
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
  
  # def inject_js(self, params):
  #   self.fs.inject_js(params)
  
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
