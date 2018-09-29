import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from json import dumps

def create_menu(menu_instance, src, eval_script, parent=None):
  for m in src:
    if "seperator" in m:
      if parent:
        parent.append(Gtk.SeparatorMenuItem())
      else:
        menu_instance.append(Gtk.SeparatorMenuItem())
      continue

    def click_handler(menuitem, callback_id, menuitem_config_obj):
      if type(menuitem) == Gtk.CheckMenuItem:
        m['checked'] = menuitem.get_active()
      
      eval_script(
        script='_macron.registeredMenuCallbacks[{}].call(null, {})'.format(
          callback_id,
          dumps(menuitem_config_obj)
        )
      )

    menuitem_obj = Gtk.MenuItem.new_with_label

    if m["isCheckable"] == True and m['submenu'] == None:
      menuitem = Gtk.CheckMenuItem(m['label'])

      if "checked" in m:
        menuitem.set_active(m['checked'])
    else:
      menuitem = Gtk.MenuItem.new_with_label(m['label'])
    
    if 'callbackID' in m:
      menuitem.connect(
        'activate',
        click_handler,
        m['callbackID'] if 'callbackID' in m else None,
        m # config obj
      )
    
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
