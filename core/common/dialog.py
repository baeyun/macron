from macron import *
from sys import path
from os import path as ospath

dirname = ospath.dirname(ospath.realpath(__file__))

if system() == "Windows":
  path.append(ospath.join(dirname, '../windows/'))
elif system() == "Linux":
  path.append(ospath.join(dirname, '../linux/'))

import dialogs

class Dialog(NativeBridge):

  @macronMethod
  def saveFile(self, config):
    # dialogs.saveFile(config)
    return dialogs.pickFile(config)
    # try:
    #   file = tkinter.filedialog.asksaveasfile(
    #     title = config['title'] if 'title' in config else 'Save file',
    #     initialdir = config['initialDirectoryPath'] if 'initialDirectoryPath' in config else None,
    #     initialfile = config['name'] if 'name' in config else None,
    #     defaultextension = config['defaultExtension'] if 'defaultExtension' in config else None,
    #     filetypes = config['fileTypes'] if 'fileTypes' in config else None,
    #     mode = 'w'
    #   )
    #   self.current_window.focus()

    #   # dialog closed with 'cancel'
    #   if not file: return False
      
    #   if "content" in config:
    #     file.write(config['content'])
      
    #   file_name = file.name
    #   file.close()
      
    #   return file_name
    # except:
    #   raise Exception('Unable to save file.')

  @macronMethod
  def pickFile(self, config):
    return dialogs.pickFile(config)

  @macronMethod
  def pickDirectory(self, config):
    dialogs.pickDirectory(config)
