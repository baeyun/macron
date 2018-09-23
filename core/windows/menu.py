from System.Windows.Controls import (
  MenuItem,
  Separator
)

def create_menu(menu_instance, src, click_handler, parent=None):
  for m in src:
    if "seperator" in m:
      if parent:
        parent.AddChild(Separator())
      else:
        menu_instance.AddChild(Separator())
      continue

    menuitem = MenuItem()
    menuitem.Header = m["header"]
    menuitem.Click += click_handler

    if "submenu" not in m:
      menuitem.IsCheckable = True if "isCheckable" in m and m["isCheckable"] == True else False
      if "checked" in m:
        menuitem.IsChecked = True if m["checked"] else False

    if "submenu" in m:
      create_menu(
        menu_instance=menu_instance,
        src=m["submenu"],
        click_handler=click_handler,
        parent=menuitem
      )

    if parent:
      parent.AddChild(menuitem)
    else:
      menu_instance.AddChild(menuitem)
      