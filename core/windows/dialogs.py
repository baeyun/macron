import clr
clr.AddReference(r"wpf\PresentationFramework")

from Microsoft.Win32 import SaveFileDialog, OpenFileDialog
from System.Windows.Forms import FolderBrowserDialog

def saveFile(config):
  dialog = SaveFileDialog()
  dialog.Title = config['title'] if 'title' in config else 'Pick file'
  dialog.FileName = config['name'];
  if 'defaultExtension' in config:
    dialog.DefaultExt = ".txt";
  # dialog.InitialDirectory = config['initialDirectory'] if 'initialDirectory' in config else None # TODO FIXME
  # dialog.Filter = "Text documents (.txt)|*.txt"; # Filter files by extension

def pickFile(config):
  dialog = OpenFileDialog()
  dialog.Title = config['title'] if 'title' in config else 'Pick file'
  # dialog.InitialDirectory = config['initialDirectory'] if 'initialDirectory' in config else None # TODO FIXME
  dialog.Multiselect = True if 'multiselect' in config and config['multiselect'] else False
  
  # # TODO FIXME
  # if 'filter' in config:
  #   for f in config['filter']:
  #     dialog.Filter = '{}|({});{}|'.format(f[0], f[1], f[1])

  result = dialog.ShowDialog()

  if result:
    if 'read' in config and config['read'] and 'multiselect' not in config:
      with open(dialog.FileName, 'r') as f:
        return f.read()
    else:
      if 'multiselect' in config and config['multiselect']:
        return list(dialog.FileNames)
      else:
        return dialog.FileName

# TODO FIXME
def pickDirectory(config):
  dialog = FolderBrowserDialog()
  dialog.Title = config['title'] if 'title' in config else 'Pick folder'
  # dialog.InitialDirectory = config['initialDirectory'] if 'initialDirectory' in config else None # TODO FIXME
  pass
