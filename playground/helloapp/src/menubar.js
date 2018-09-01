// const { Menu } = require('macron')
let Menu = function (menu) { return menu }
Menu.SEPERATOR = {seperator: true}

module.exports = new Menu([
  {
    header: "File",
    submenu: [
      {header: "New File", callback: "create_file"},
      {header: "New Window", callback: "create_window"},
      Menu.SEPERATOR,
      {header: "Open File", callback: "open_file"},
      {header: "Open Folder", callback: "open_folder"},
      Menu.SEPERATOR,
      {header: "Open recent", submenu: [
        {header: "./views/CodeEditor/index.js", callback: "open_recent"},
        {header: "../components/windows/MenuButton", callback: "open_recent"},
        {header: "./guppy/scripts/", callback: "openrecent"},
        {header: "../static/img/logo.png", callback: "open_recent"},
        {header: "../vsnative/", callback: "open_recent"}
      ]},
      Menu.SEPERATOR,
      {header: "Save", callback: "save"},
      {header: "Save As", callback: "save_as"},
      {header: "Save All", callback: "save_all"},
      Menu.SEPERATOR,
      {header: "Auto Save", isCheckable: true, checked: true, callback: "toggle_auto_save"},
      Menu.SEPERATOR,
      {header: "Preferences", callback: "open_preference_settings"},
      Menu.SEPERATOR,
      {header: "Revert File", callback: "revert_file"},
      {header: "Close Editor", callback: "close_editor"},
      {header: "Close Folder", callback: "close_folder"},
      {header: "Close Window", callback: "close_window"}
    ]
  },
  {header: "Edit", submenu: [
    {header: "Word Wrap", isCheckable: true}
  ]},
  {header: "Selection"},
  {header: "View"},
  {header: "Go", submenu: [
    {header: "Share", icon: "&#xE72D;"},
    {header: "Copy"},
    {header: "Delete"},
  ]},
  {header: "Debug"},
  {header: "Tasks"},
  {header: "Help"}
])