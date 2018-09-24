import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from menu import create_menu

class MacronMenubar:

  def __init__(self, window):
    self.menu = Gtk.MenuBar.new()

    create_menu(
      self.menu,
      window.config['menu'],
      window.webview.evaluate_script
    )

  def get_menu(self):
    return self.menu
