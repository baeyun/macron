from macron import *
import sys
from os import path
from platform import system
from System.Windows.Controls import ContextMenu

dirname = path.dirname(path.realpath(__file__))

if system() == "Windows":
  sys.path.append(path.join(dirname, '../windows/'))
elif system() == "Linux":
  sys.path.append(path.join(dirname, '../linux/'))

from menu import create_menu

context_menus = {}

class _ContextMenu(NativeBridge):

  @macronMethod
  def spawn(self, query, menu_src):
    if system() == 'Windows':
      if query in context_menus:
        self.current_window.ContextMenu = context_menus[query]
        self.current_window.ContextMenu.IsOpen = True
      else:
        # self.current_window.ContextMenu.script_callback = 'contextmenu_callback_function'
        cm = ContextMenu()
        context_menus[query] = cm
        self.current_window.ContextMenu = cm
        create_menu(cm, menu_src, self.menu_item_click)
        cm.HorizontalOffset = 7
        cm.IsOpen = True
    elif system() == 'Linux':
      print('linux context')

  # TODO handle event
  def menu_item_click(self, sender, args):
    print(sender)
    pass
