from System.Windows.Controls import (
  MenuItem,
  Separator
)
from functools import partial
from json import dumps
import re

_menubar_item_callback_id = 0

def create_menu(menu_instance, src, eval_script, parent=None):
  global _menubar_item_callback_id

  for m in src:
    if 'clickCallback' in m:
      m['callbackID'] = _menubar_item_callback_id
      _menubar_item_callback_id += 1

      eval_script(
        script='_macron.menubarCallbacks[{}] = {}'.format(
          m['callbackID'],
          multiple_replace(m['clickCallback'], {
            '/n': '\n',
            '/r': '\r'
          })
        )
      )

    if "seperator" in m:
      if parent:
        parent.AddChild(Separator())
      else:
        menu_instance.AddChild(Separator())
      continue

    # TODO improve
    class ClickCallbackWrapper:
      def __init__(self, menuitem_config):
        self.menuitem_config = menuitem_config
      
      def click_handler(self, sender, args):
        if sender.IsCheckable:
          self.menuitem_config['checked'] = sender.IsChecked
        
        if 'callbackID' in self.menuitem_config:
          eval_script(
            script='_macron.{}[{}].call(null, {})'.format(
              'contextmenuCallbacks' if self.menuitem_config['type'] == 'contextmenuitem' else 'menubarCallbacks',
              self.menuitem_config['callbackID'],
              dumps(self.menuitem_config)
            ),
            on_ready=False
          )

    menuitem = MenuItem()
    menuitem.Header = m["label"]
    click_wrapper = ClickCallbackWrapper(m) # config obj
    menuitem.Click += click_wrapper.click_handler

    if m["isCheckable"] == True and m['submenu'] == None:
      menuitem.IsCheckable = True
      if "checked" in m and m["checked"] != None:
        menuitem.IsChecked = m["checked"]

    if "submenu" in m and m['submenu']:
      create_menu(
        menu_instance=menu_instance,
        src=m["submenu"],
        eval_script=eval_script,
        parent=menuitem
      )

    if parent:
      parent.AddChild(menuitem)
    else:
      menu_instance.AddChild(menuitem)

def multiple_replace(text, adict):
  rx = re.compile('|'.join(map(re.escape, adict)))
  def one_xlat(match):
    return adict[match.group(0)]
  return rx.sub(one_xlat, text)
