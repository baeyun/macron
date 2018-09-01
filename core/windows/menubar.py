from System import Array
from System.Windows.Controls import Menu, MenuItem, Separator
from System.Windows import Thickness

class MacronMenubar:

  def __init__(self, src):

    self.menu = Menu()

    # self.menu_thickness = Thickness()
    # self.menu_thickness.Bottom = 0
    # self.menu_thickness.Left = 0
    # self.menu_thickness.Right = 0
    # self.menu_thickness.Top = 0

    self.create_menu(src)

    self.menu.IsMainMenu = True

  def create_menu(self, src, parent=None):

    for m in src:
      if "seperator" in m:
        if parent:
          parent.AddChild(Separator())
        continue

      menuitem = MenuItem()
      menuitem.Header = m["header"]
      menuitem.Click += self.menu_item_click
      # menuitem.BorderThickness = self.menu_thickness

      if "submenu" not in m:
        menuitem.IsCheckable = True if "isCheckable" in m and m["isCheckable"] == True else False
        if "checked" in m:
          menuitem.IsChecked = True if m["checked"] else False

      if "submenu" in m:
        self.create_menu(src=m["submenu"], parent=menuitem)

      if parent:
        parent.AddChild(menuitem)
      else:
        self.menu.AddChild(menuitem)

    # menu_source = Array[MenuItem]([submenuitem1, submenuitem2])
    # menu.ItemsSource = menu_source

  def get_menu(self):
    return self.menu

  # TODO handle event
  def menu_item_click(self, sender, args):
    return
