import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MacronMenubar:

  def __init__(self, src):
    self.menu = Gtk.MenuBar.new()

    self.create_menu(src)

  def create_menu(self, src, parent=None):

    for m in src:
      if "seperator" in m:
        if parent:
          parent.append(Gtk.SeparatorMenuItem())
        continue

      menuitem_obj = Gtk.MenuItem.new_with_label

      if "submenu" not in m and "isCheckable" in m and m["isCheckable"]:
        menuitem_obj = Gtk.CheckMenuItem

      menuitem = menuitem_obj(m["header"])
      menuitem.connect('activate', self.menu_item_click)
      
      if "checked" in m and m["checked"]:
        menuitem.set_active(True)
      
      if "submenu" in m:
        submenu = Gtk.Menu.new()
        self.create_menu(src=m["submenu"], parent=submenu)
        menuitem.set_submenu(submenu)

      if parent:
        parent.append(menuitem)
      else:
        self.menu.append(menuitem)

  def get_menu(self):
    return self.menu

  # TODO handle event
  def menu_item_click(self, menuitem):
    return
