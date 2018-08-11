import sys
from os import getcwd, fsync
from json import loads
import webview
import chalk
import threading

class NewtronCoreAPI:
  def __init__(self, logfile_stream):
    self.logfile_stream = logfile_stream
    self.window_title = "New Window"
    self.window_uid = None

  def log(self, params):
    # Convert webview-generated tuples to strings before writing
    self.logfile_stream.write(''.join(params["toLog"]))
    # Saves immediately without waiting for close
    self.logfile_stream.flush()
    # Ensures file is synced with latest changes
    fsync(self.logfile_stream.fileno())

    return

  def createWindow(self, config):
    if self.window_uid:
      return
    # title=config["title"] if config["title"] else "New Window",
    # url=config["url"] if config["url"] else "",
    # js_api=config["nativeAPI"] if config["nativeAPI"] else None,
    # width=config["width"] if config["width"] else 800,
    # height=config["height"] if config["height"] else 600,
    # resizable=config["resizable"] if config["resizable"] else True,
    # fullscreen=config["fullscreen"] if config["fullscreen"] else False,
    # min_size=(
    #   config["minWidth"] if config["minWidth"] else 200,
    #   config["minHeight"] if config["minHeight"] else 100
    # ),
    # strings=config["strings"] if config["strings"] else {},
    # confirm_quit=config["confirmQuit"] if config["confirmQuit"] else False,
    # background_color=config["backgroundColor"] if config["backgroundColor"] else '#FFF',
    # debug=config["debug"] if config["debug"] else False,
    # text_select=config["userSelect"] if config["userSelect"] else False

    self.window_title = ''.join(config["title"])

    self.window_uid = webview.create_window(
      title=''.join(config["title"]),
      url=''.join(config["url"]),
      # js_api=''.join(config["js_api"]),
      # width=''.join(config["width"]),
      # height=''.join(config["height"]),
      # resizable=''.join(config["resizable"]),
      # fullscreen=''.join(config["fullscreen"]),
      # min_size=''.join(config["min_size"]),
      # strings=''.join(config["strings"]),
      # confirm_quit=''.join(config["confirm_quit"]),
      # background_color=''.join(config["background_color"]),
      # debug=''.join(config["debug"]),
      # text_select=''.join(config["text_select"])
    )

  def closeWindow(self, params):
    if not self.window_uid:
      chalk.chalk("red")("A valid uid is required to close a window. Either a window was not created or uid does not exist.")

    webview.destroy_window(uid=self.window_uid)
    self.window_uid = None
  
  def getCurrentURL(self, uid):
    return webview.get_current_url(uid=''.join(uid))
  
  # File dialogs
  def openFileDialog(self, params):
    file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
    files = webview.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)

    return files
  
  # Quit application
  def quitApplication(self, uid):
    # @todo Handle destroy error (internal)
    # @todo Close self.logfile_stream
    self.logfile_stream.close()
    try:
      webview.destroy_window(uid=uid)
    except Exception as e:
      print(e)
    
    return