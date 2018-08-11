import os
import sys
import chalk
import webview

class Window:
  def __init__(self):
    self.window_title = "New Window"
    self.window_uid = None
  
  def create(self, config):
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

    return self

  def close(self):
    if not self.window_uid:
      chalk.chalk("red")("A valid uid is required to close a window. Either a window was not created or uid does not exist.")

    webview.destroy_window(uid=self.window_uid)
    self.window_uid = None
    
    return self
  
  # def get_url(self, uid):
  #   return webview.get_current_url(uid=''.join(uid))

  # Quit application
  def quit(self):
    # @todo Handle destroy error (internal)
    try:
      webview.destroy_window(uid='master')
    except Exception as e:
      print(e)
    
    return