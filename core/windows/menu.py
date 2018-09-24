from System.Windows.Controls import (
  MenuItem,
  Separator
)

def create_menu(menu_instance, src, eval_script, parent=None):
  for m in src:
    if "seperator" in m:
      if parent:
        parent.AddChild(Separator())
      else:
        menu_instance.AddChild(Separator())
      continue

    def click_handler(sender, args):
      if sender.Tag:
        eval_script(
          script='''({})()'''.format(
            sender.Tag.replace('/n', ' ').replace('/r', '')
          ),
          on_ready=False
        )
        print('''({})()'''.format(
          sender.Tag
        ))

    menuitem = MenuItem()
    menuitem.Header = m["header"]
    if 'click' in m:
      menuitem.Tag = m["click"]
    menuitem.Click += click_handler

    if "submenu" not in m:
      menuitem.IsCheckable = True if "isCheckable" in m and m["isCheckable"] == True else False
      if "checked" in m:
        menuitem.IsChecked = True if m["checked"] else False

    if "submenu" in m:
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
      