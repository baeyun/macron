import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from json import dumps
import re

_menubar_item_callback_id = 0

def create_menu(menu_instance, src, eval_script, parent=None):
  global _menubar_item_callback_id
  
  for m in src:
    if "seperator" in m:
      if parent:
        parent.append(Gtk.SeparatorMenuItem())
      else:
        menu_instance.append(Gtk.SeparatorMenuItem())
      continue

    if 'clickCallback' in m:
      m['callbackID'] = _menubar_item_callback_id
      _menubar_item_callback_id += 1

      eval_script(
        script='_macron.menubarCallbacks.push({})'.format(
          multiple_replace(m['clickCallback'], {
            '/n': '\n',
            '/r': '\r'
          })
        )
      )

    def click_handler(menuitem, menuitem_config):
      if type(menuitem) == Gtk.CheckMenuItem:
        menuitem_config['checked'] = menuitem.get_active()
      
      if 'callbackID' in menuitem_config:
        eval_script(
          script='_macron.{}[{}].call(null, {})'.format(
            'contextmenuCallbacks' if menuitem_config['type'] == 'contextmenuitem' else 'menubarCallbacks',
            menuitem_config['callbackID'],
            dumps(menuitem_config)
          )
        )

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

def multiple_replace(text, adict):
  rx = re.compile('|'.join(map(re.escape, adict)))
  def one_xlat(match):
    return adict[match.group(0)]
  return rx.sub(one_xlat, text)
