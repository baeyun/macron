import os
import sys
import chalk
import webview

class Window:
  def __init__(self):
    self.window_uid = None
  
  def create(self, config):
    if self.window_uid:
      return

    title=''.join(config["title"]) if "title" in config else "New Window"
    url=''.join(config["url"]) if "url" in config else ""
    # js_api=config["nativeAPI"] if "nativeAPI" in config else None
    width=config["width"] if "width" in config else 800
    height=config["height"] if "height" in config else 600
    resizable=config["resizable"] if "resizable" in config else True
    fullscreen=config["fullscreen"] if "fullscreen" in config else False
    min_size=(
      config["minWidth"] if "minWidth" in config else 200,
      config["minHeight"] if "minHeight" in config else 100
    )
    strings=config["strings"] if "strings" in config else {}
    confirm_quit=config["confirmQuit"] if "confirmQuit" in config else False
    background_color=''.join(config["backgroundColor"]) if "backgroundColor" in config else '#FFF'
    debug=config["debug"] if "debug" in config else False
    text_select=config["userSelect"] if "userSelect" in config else False

    self.window_uid = webview.create_window(
      title=title,
      url=url,
      # js_api=js_api,
      width=width,
      height=height,
      resizable=resizable,
      fullscreen=fullscreen,
      min_size=min_size,
      strings=strings,
      confirm_quit=confirm_quit,
      background_color=background_color,
      debug=debug,
      text_select=text_select
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