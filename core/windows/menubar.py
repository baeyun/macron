from System.Windows.Controls import Menu
from menu import create_menu

class MacronMenubar(Menu):

  def __init__(self, window):

    self.IsMainMenu = True

    create_menu(
      self,
      window.config['menu'],
      window.webview.evaluate_script
    )

  def get_menu(self):
    return self
