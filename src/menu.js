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
      _macron.registeredMenuCallbacks.push(
        menuitem.click
      )
      newMenuitem.callbackID = _macron.registeredMenuCallbacks.length - 1
    }

    return newMenuitem
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = Menu
} else {
  macron.Menu = Menu
}
