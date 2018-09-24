from macron import *
import sys
from os import path
from platform import system

dirname = path.dirname(path.realpath(__file__))

if system() == "Windows":
  from System.Windows.Controls import ContextMenu
  sys.path.append(path.join(dirname, '../windows/'))
elif system() == "Linux":
  import gi
  gi.require_version('Gtk', '3.0')
  from gi.repository import Gtk
  sys.path.append(path.join(dirname, '../linux/'))

from menu import create_menu

_registered_contextmenus = {}

class _ContextMenu(NativeBridge):

  @macronMethod
  def spawn(self, query, menu_src):
    if system() == 'Windows':
      if query in _registered_contextmenus:
        self.current_window.ContextMenu = _registered_contextmenus[query]
        self.current_window.ContextMenu.IsOpen = True
      else:
        cm = ContextMenu()
        _registered_contextmenus[query] = cm
        self.current_window.ContextMenu = cm
        create_menu(
          cm,
          menu_src,
          self.context.evaluate_script
        )
        cm.HorizontalOffset = 7
        cm.IsOpen = True
    elif system() == 'Linux':
      if query in _registered_contextmenus:
        self.context.popup = _registered_contextmenus[query]
        self.context.connect('button-release-event', self.button_release_event)
      else:
        self.context.popup = Gtk.Menu()
        create_menu(
          self.context.popup,
          menu_src,
          self.context.evaluate_script
        )
        self.context.popup.show_all()
        self.context.connect('button-release-event', self.button_release_event)
        _registered_contextmenus[query] = self.context.popup

  # Linux only
  def button_release_event(self, button, event):
    if event.button == 3:
        self.context.popup.popup(None, None, None, None, event.button, event.time)
