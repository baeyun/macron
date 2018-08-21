import gi
import sys
import time
import threading

gi.require_version("Gtk", "3.0")

from gi.repository import GLib, Gtk, GObject, Gdk

class MacronWindow(Gtk.Window):
  def __init__(self, config):
    self.title = "Hello World"
    self.window = Gtk.Window(
      title=self.title,
      default_height=500,
      default_width=500
    )
    self.window.connect("destroy", Gtk.main_quit)
    
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

    # Gets or sets the resizable property of the window
    # False by default
    # self.resizable = False
    # self.window.set_resizable(self.resizable)

    # Focus on window on when created
    # self.focus_on_startup = False if not self.window.get_focus_on_map() else True
    # self.window.set_focus_on_map(self.focus_on_start)

    # Sets whether the window should have a taskbar button
    # self.hide_from_taskbar = True
    # self.window.set_skip_taskbar_hint(self.hide_from_taskbar)

    # FIXME: The hide property should work as expected
    # self.hide_on_startup = False
    # self.window.hide()

    # TODO: Start from center of parent if parent exists
    # self.startup_from_center = True
    # if self.startup_from_center == True:
    #   self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

    # Determines if window should start maximized or minimized
    # self.startup_state = "minimized"
    # if self.startup_state == "maximized":
    #   self.window.maximize()
    # elif self.startup_state == "minimized":
    #   self.window.iconify()

    # Determines whether window should be frameless or not
    # self.frameless = False
    # self.window.set_decorated(self.frameless)

    # TODO: Handle window events
  
  def focus(self):
    self.window.set_focus_on_map(self.focus_on_start)
  
  def hide(self):
    self.window.hide()
  
  def close(self):
    self.window.close()

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
