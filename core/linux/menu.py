import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_menu(menu_instance, src, eval_script, parent=None):
  for m in src:
    if "seperator" in m:
      if parent:
        parent.append(Gtk.SeparatorMenuItem())
      else:
        menu_instance.append(Gtk.SeparatorMenuItem())
      continue

    def click_handler(menuitem, callbackID):
      eval_script(
        script='_macron.registeredMenuCallbacks[{}].call()'.format(
          callbackID
        )
      )

    menuitem_obj = Gtk.MenuItem.new_with_label

    if "submenu" not in m and not m['submenu'] and "isCheckable" in m and m["isCheckable"]:
      menuitem_obj = Gtk.CheckMenuItem

    menuitem = menuitem_obj(m['label'])
    
    if 'callbackID' in m:
      menuitem.connect(
        'activate',
        click_handler,
        m['callbackID'] if 'callbackID' in m else None
      )
    
    if "submenu" not in m and not m['submenu'] and "isCheckable" in m and m["isCheckable"] and "checked" in m:
      menuitem.set_active(m["checked"])
    
    if "submenu" in m and m['submenu']:
      submenu = Gtk.Menu.new()
      create_menu(
        menu_instance=menu_instance,
        src=m["submenu"],
        eval_script=eval_script,
        parent=submenu
      )
      menuitem.set_submenu(submenu)

    if parent:
      parent.append(menuitem)
    else:
      menu_instance.append(menuitem)
