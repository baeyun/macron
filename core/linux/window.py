import gi
import sys
import threading

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

from webview import MacronWebview

class MacronWindow(Gtk.Window):
  def __init__(self, config):
    self.title = config["title"]
    self.window = Gtk.Window(
      title=self.title,
      default_height=config["height"] if "height" in config else 500,
      default_width=config["height"] if "height" in config else 500
    )
    self.window.connect("destroy", Gtk.main_quit)
    # self.win_webview = MacronWebview("No config for now!!")
    # self.window.add(self.win_webview.webview)
    
    # Dimensions & Geometry
    # These properties are just maps for the original
    # GTK Window size setter and getter methods.
    # self.width = 500
    # self.height = 1000

    # self.window.set_default_size(
    #   self.width,
    #   self.height
    # )

    # self.max_height = 500
    # self.max_width = 500
    # self.min_height = 500
    # self.min_width = 500

    # gh = Gdk.Geometry()
    # gh.min_width = self.min_width
    # gh.min_height = self.min_height
    # gh.max_width = self.max_width
    # gh.max_height = self.max_height

    # self.window.set_geometry_hints(
    #   self.window,
    #   Gdk.WindowHints.ASPECT,
    #   Gdk.Geometry
    # )

    # self.is_active = None
    # self.is_focused = None
    # self.is_keyboard_focused = None
    # self.is_visible = None

    # Gets or sets the resizable property of the window.
    # False by default.
    self.resizable = config["resizable"] if "resizable" in config else True
    self.window.set_resizable(self.resizable)

    # Focus on window on when created.
    self.focus_on_startup = config["focusOnStartup"] if "focusOnStartup" in config else True
    self.window.set_focus_on_map(self.focus_on_startup)

    # Sets whether the window should have a taskbar button.
    self.hide_in_taskbar = config["hideInTaskbar"] if "hideInTaskbar" in config else False
    self.window.set_skip_taskbar_hint(self.hide_in_taskbar)
  
    # FIXME: The hide property should work as expected
    # HACK: Possible workaround is to set:
    #    hideInTaskbar: true,
    #    startupState: "minimized"
    # THIS 'SIMULATES' REAL 'window.hide()'
    # from the macron.config.js file or any other window loader.


    # self.hide_on_startup = config["hideOnStartup"] if "hideOnStartup" in config else False
    # if self.hide_on_startup:
    #   self.window.hide()

    # Centers window to screen's center.
    # self.startup_from_center = True
    if "startupFromCenter" in config and config["startupFromCenter"] == True:
      self.window.set_position(Gtk.WindowPosition.CENTER)

    # Determines if window should start maximized or minimized.
    self.startup_state = config["startupState"] if "startupState" in config else "normal"
    if self.startup_state == "maximized":
      self.window.maximize()
    elif self.startup_state == "minimized":
      self.window.iconify() # minimizes

    # Determines whether window should be frameless or not.
    # self.frameless = False
    if "frameless" in config and config["frameless"] == True:
      self.window.set_decorated(False) # False means there is no frame.

    # TODO: Handle window events
  
  # def focus(self):
  #   self.window.set_focus_on_map(self.focus_on_start)
  
  # def hide(self):
  #   self.window.hide()
  
  # def close(self):
  #   self.window.close()

def create_window(config):
  def create():
    MacronWindow(config=config).window.show_all()
  
  # thread = threading.Thread(target=create)
  # thread.daemon = True
  # thread.start()
  create()
  Gtk.main()
    

if __name__ == "__main__":
  create_window("No config for now!!!")
