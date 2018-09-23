from menu import create_menu
from System.Windows.Controls import Menu

class MacronMenubar(Menu):

  def __init__(self, src):

    self.IsMainMenu = True

    create_menu(self, src, self.menu_item_click)

    return self

  # TODO handle event
  def menu_item_click(self, sender, args):
    return
