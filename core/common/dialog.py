from macron import NativeBridge

from os import fstat
import tkinter as tk
from tkinter.filedialog import asksaveasfile, askopenfilename, askdirectory

# Singleton instance of tkinter
root = tk.Tk()
# Hide tkinter window
root.withdraw()

class Dialog(NativeBridge):

  def alert(self):
    pass

  def warn(self):
    pass

  def error(self):
    pass
    
  def info(self):
    pass

  def fileSaver(self, config):
    try:
      file = asksaveasfile(
        title = config['title'] if 'title' in config else 'Save file',
        initialdir = config['dirName'] if 'dirName' in config else None,
        initialfile = config['name'] if 'name' in config else None,
        defaultextension = config['extension'] if 'extension' in config else None,
        filetypes = config['fileTypes'] if 'fileTypes' in config else None,
        mode = 'w'
      )
      self.window.focus()

      # dialog closed with "cancel".
      if not file:
        return False
      
      if "content" in config:
        file.write(config['content'])
        file_name = file.name
        file.close()
        return file_name
    except:
      raise Exception('Unable to save file.')

  def filePicker(self):
    try:
      file_path = askopenfilename(filetypes=(("Template files", "*.tplate"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")))
      self.window.focus()
      return file_path
    except:
      raise Exception('Unable to select file.')

  def dirPicker(self):
    try:
      dir_path = askdirectory()
      self.window.focus()
      return dir_path
    except:
      raise Exception('Unable to select directory.')
