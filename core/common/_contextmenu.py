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
    self.context.evaluate_script("(function() { document.querySelector('#text').style.color = 'red' })()")
    if system() == 'Windows':
      if query in context_menus:
        self.current_window.ContextMenu = context_menus[query]
        self.current_window.ContextMenu.IsOpen = True
      else:
        cm = ContextMenu()
        context_menus[query] = cm
        self.current_window.ContextMenu = cm
        create_menu(
          cm,
          menu_src,
          self.context.evaluate_script
        )
        cm.HorizontalOffset = 7
        cm.IsOpen = True
    elif system() == 'Linux':
      print('linux context')
