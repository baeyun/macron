import gi
import sys
import threading

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

# import tkinter
from tkinter import Tk
from webview import MacronWebview

class MacronWindow(Gtk.Window):
  
  def __init__(self, config):
    # Single hidden tkinter instance for app
    Tk().withdraw()

    self.config = config

    # Initialize main window
    self.window = Gtk.Window(
      title=config["title"] if "title" in config else "New Window",
      default_height=config["height"] if "height" in config else 500,
      default_width=config["height"] if "height" in config else 500
    )
    self.window.connect("destroy", Gtk.main_quit)
    if "maxHeight" in config: self.max_height(config["maxHeight"])
    if "maxWidth" in config: self.max_width(config["maxWidth"])
    if "minHeight" in config: self.min_height(config["minHeight"])
    if "minWidth" in config: self.min_width(config["minWidth"])
    self.resizable(config["resizable"])
    self.focus_on_startup(config["focusOnStartup"])
    self.hide_in_taskbar(config["hideInTaskbar"])
    self.hide_on_startup(config["hideOnStartup"])
    self.startup_from_center(config["startupFromCenter"])
    self.state(config["startupState"])
    if config["frameless"]: self.frameless(True)

    self.webview = MacronWebview(current_window=self, config=config)
    
    self.window.add(self.webview)
  
  def title(self, title):
    if title != None:
      self.window.set_title(title)
    else:
      return self.window.get_title()
  
  def height(self, height):
    if height != None:
      self.window.set_default_size(self.window.get_default_size()[0], height)
    else:
      return self.window.get_default_size()[1]
  
  def width(self, width):
    if width != None:
      self.window.set_default_size(width, self.window.get_default_size()[1])
    else:
      return self.window.get_default_size()[0]
  
  def max_height(self, max_height):
    if max_height != None:
      self.window.set_max_height(max_height)
    else:
      return self.window.get_max_height()
  
  def max_width(self, max_width):
    if max_width != None:
      self.window.set_max_width(max_width)
    else:
      return self.window.get_max_width()
  
  def min_height(self, min_height):
    if min_height != None:
      self.min_height_size = min_height
      min_width = self.min_width_size if hasattr(self, 'min_width_size') else 0
      
      self.window.set_size_request(min_width, min_height)
    else:
      return self.window.get_min_height()
  
  def min_width(self, min_width):
    if min_width != None:
      self.min_width_size = min_width
      min_height = self.min_height_size if hasattr(self, 'min_height_size') else 0

      self.window.set_size_request(min_width, min_height)
    else:
      return self.window.get_min_width()
  
  def resizable(self, resizable):
    if resizable != None:
      self.window.set_resizable(resizable)
    else:
      return self.window.get_resizable()
  
  def focus_on_startup(self, focus_on_startup):
    if focus_on_startup != None:
      self.window.set_focus_on_map(focus_on_startup)
    else:
      return self.window.get_focus_on_map()
  
  def hide_in_taskbar(self, hide_in_taskbar):
    if hide_in_taskbar != None:
      self.window.set_skip_taskbar_hint(hide_in_taskbar)
    else:
      return self.window.get_skip_taskbar_hint()
  
  def hide_on_startup(self, hide_on_startup):
    if hide_on_startup == True:
      self.window.hide()
  
  def startup_from_center(self, startup_from_center):
    if startup_from_center != None:
      self.window.set_position(Gtk.WindowPosition.CENTER)
    else:
      return self.window.get_position()
  
  def state(self, state):
    if state != None:
      if state == "maximized":
        self.window.maximize()
      elif state == "minimized":
        self.window.iconify()
      elif state == "normal":
        # TODO test
        # self.window.deiconify()
        pass
    else:
      if gtk.gdk.WINDOW_STATE_MAXIMIZED:
        return "maximized"
      elif gtk.gdk.WINDOW_STATE_ICONIFIED:
        return "minimized"
      else:
        return "normal"
  
  def frameless(self, frameless):
    if frameless != None:
      self.window.set_decorated(not frameless)
    else:
      return self.window.get_decorated()

  def activate(self):
    return self.window.activate_focus()
    # return self.window.activate_default()

  def focus(self):
    # TODO test
    return self.window.set_focus()

  def hide(self):
    self.window.hide()

  def show(self):
    self.window.show_all()
      
  def close(self):
    self.window.close()

  """"""""""""""""""""""" Events """""""""""""""""""""""

  # Occurs when a window becomes the foreground window.
  def on_activated(self, sender, args):
    self.webview.triggerEvent('activate')

  # Occurs when the window is about to close.
  def on_closed(self, sender, args):
    self.webview.triggerEvent('close')

  # Occurs directly after Close() is called, and can be handled to cancel window closure.
  def on_closing(self, sender, args):
    self.webview.triggerEvent('closing')

  # Occurs just before any context menu on the element is closed.
  def on_contextmenuclosing(self, sender, args):
    self.webview.triggerEvent('contextMenuClose')

  # Occurs when any context menu on the element is opened.
  def on_contextmenuopening(self, sender, args):
    self.webview.triggerEvent('contextMenuOpen')

  # Occurs when a window becomes a background window.
  def on_deactivated(self, sender, args):
    self.webview.triggerEvent('deactivate')

  # Occurs when the value of the Focusable property changes.
  def on_focusablechanged(self, sender, args):
    self.webview.triggerEvent('focusChange')

  # Occurs when a key is pressed while focus is on this element.
  def on_previewkeydown(self, sender, args):
    self.webview.triggerEvent('keydown')

  # Occurs when a key is released while focus is on this element.
  def on_previewkeyup(self, sender, args):
    self.webview.triggerEvent('keyup')

  # Occurs when either the ActualHeight or the ActualWidth properties change value on this element.
  def on_sizechanged(self, sender, args):
    self.webview.triggerEvent('sizeChange')

  # Occurs when the window's WindowState property changes.
  def on_statechanged(self, sender, args):
    self.webview.triggerEvent('stateChange')
  

def create_window(config):
  def create():
    MacronWindow(config=config).show()
  
  # thread = threading.Thread(target=create)
  # thread.daemon = True
  # thread.start()
  create()
  Gtk.main()
    

if __name__ == "__main__":
  create_window("No config for now!!!")
