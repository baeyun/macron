from macron import *

from tkinter.filedialog import (
  asksaveasfile,
  askopenfilename,
  askopenfilenames,
  askdirectory
)

class Dialog(NativeBridge):

  @macronMethod
  def fileSaver(self, config):
    try:
      file = asksaveasfile(
        title = config['title'] if 'title' in config else 'Save file',
        initialdir = config['initialDirectoryPath'] if 'initialDirectoryPath' in config else None,
        initialfile = config['name'] if 'name' in config else None,
        defaultextension = config['defaultExtension'] if 'defaultExtension' in config else None,
        filetypes = config['fileTypes'] if 'fileTypes' in config else None,
        mode = 'w'
      )
      self.window.focus()

      # dialog closed with 'cancel'
      if not file: return False
      
      if "content" in config:
        file.write(config['content'])
      
      file_name = file.name
      file.close()
      
      return file_name
    except:
      raise Exception('Unable to save file.')

  @macronMethod
  def filePicker(self, config):
    try:
      config_opts = {
        'title': config['title'] if 'title' in config else 'Save file',
        'initialdir': config['initialDirectoryPath'] if 'initialDirectoryPath' in config else None,
        'filetypes': config['fileTypes'] if 'fileTypes' in config else None
      }
      self.window.focus()

      if 'allowMultiPick' in config and config['allowMultiPick']:
        file_paths = askopenfilenames(**config_opts)
        
        # dialog closed with 'cancel'
        if not file_paths: return False
        
        return file_paths
      else:
        file_path = askopenfilename(**config_opts)
        
        # dialog closed with 'cancel'
        if not file_path: return False

        if 'read' in config and config['read']:
          with open(file_path, 'r') as f:
            return f.read()
        
        return file_path
    except:
      raise Exception('Unable to select file.')

  @macronMethod
  def directoryPicker(self, config):
    try:
      dir_path = askdirectory(
        title = config['title'] if 'title' in config else 'Save file',
        initialdir = config['initialDirectoryPath'] if 'initialDirectoryPath' in config else None
      )
      self.window.focus()

      # dialog closed with 'cancel'
      if not dir_path: return False

      return dir_path
    except:
      raise Exception('Unable to select directory.')
