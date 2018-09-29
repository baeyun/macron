// macron.Menu Constants API

var Menu = {
  Seperator: {seperator: true},
  MenuItem: function(menuitem) {
    var newMenuitem = {
      label: menuitem.label,
      isCheckable: menuitem.isCheckable || null,
      checked: menuitem.checked || false,
      submenu: menuitem.submenu || null
    }

    if (menuitem.click && typeof module === 'undefined') {
      newMenuitem.type = 'contextmenuitem'
      _macron.contextmenuCallbacks.push(
        menuitem.click
      )
      newMenuitem.callbackID = _macron.contextmenuCallbacks.length - 1
    } else if (menuitem.click) {
      newMenuitem.type = 'menubaritem'
      newMenuitem.clickCallback = menuitem.click.toString()
    }

    return newMenuitem
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = Menu
} else {
  macron.Menu = Menu
}
