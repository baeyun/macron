import gi
import sys
import threading

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

from webview import MacronWebview
from bridge import MacronBridge

class MacronWindow(Gtk.Window):
  def __init__(self, config):
    self.window = Gtk.Window(
      title=config["title"] if "title" in config else "New Window",
      default_height=config["height"] if "height" in config else 500,
      default_width=config["height"] if "height" in config else 500
    )
    self.window.connect("destroy", Gtk.main_quit)

    self.webview = MacronWebview(config={
      "devServerURI": config["devServerURI"] if "devServerURI" in config else "https://localhost:3000",
    }).webview

    self.bridge = MacronBridge(webview=self.webview)
    
    self.window.add(self.webview)

    self.resizable(False)
  
  def title(self, title):
    if title:
      self.window.set_title(title)
  
  def height(self, height):
    if height:
      self.window.set_default_size(self.window.get_default_size()[0], height)
  
  def width(self, width):
    if width:
      self.window.set_default_size(width, self.window.get_default_size()[1])
  
  # def max_height(self, max_height):
  #   if max_height:
  #     self.window.set_max_height(max_height)
  
  # def max_width(self, max_width):
  #   if max_width:
  #     self.window.set_max_width(max_width)
  
  # def min_height(self, min_height):
  #   if min_height:
  #     self.window.set_min_height(min_height)
  
  # def min_width(self, min_width):
  #   if min_width:
  #     self.window.set_min_width(min_width)
  
  def resizable(self, resizable):
    if resizable:
      self.window.set_resizable(resizable)
  
  def focus_on_startup(self, focus_on_startup):
    if focus_on_startup:
      self.window.set_focus_on_map(focus_on_startup)
  
  def hide_in_taskbar(self, hide_in_taskbar):
    if hide_in_taskbar:
      self.window.set_skip_taskbar_hint(hide_in_taskbar)
  
  def hide_on_startup(self, hide_on_startup):
    if hide_on_startup == True:
      self.window.hide()
  
  def startup_from_center(self, startup_from_center):
    if startup_from_center:
      self.window.set_position(Gtk.WindowPosition.CENTER)
  
  def state(self, state):
    if state:
      if state == "maximized":
        self.window.maximize()
      elif state == "minimized":
        self.window.iconify()
      elif state == "normal":
        # self.window.deiconify()
        pass
      # if self.WindowState == 2:
      #   return "maximized"
      # elif self.WindowState == 1:
      #   return "minimized"
      # elif self.WindowState == 0:
      #   return "normal"
  
  def frameless(self, frameless):
    if frameless:
      self.window.set_decorated(not frameless)
      
  def close(self):
    self.window.close()

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
