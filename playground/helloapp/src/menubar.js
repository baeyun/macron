// const { Menu, MenuItem } = require('macron')

module.exports = [
  {
    name: "File",
    submenu: [
      {name: "New File", callback: "CREATE_FILE"},
      {name: "New Window", callback: "CREATE_WINDOW"},
      {seperator: true},
      {name: "Open File", callback: "OPEN_FILE"},
      {name: "Open Folder", callback: "OPEN_FOLDER"},
      {seperator: true},
      {name: "Open recent", submenu: [ // @todo get from store
        {name: "./views/CodeEditor/index.js", callback: "OPEN_RECENT"},
        {name: "../components/windows/MenuButton", callback: "OPEN_RECENT"},
        {name: "./guppy/scripts/", callback: "openRecent"},
        {name: "../static/img/logo.png", callback: "OPEN_RECENT"},
        {name: "../vsnative/", callback: "OPEN_RECENT"}
      ]},
      {seperator: true},
      {name: "Save", callback: "save"},
      {name: "Save As", callback: "SAVE_AS"},
      {name: "Save All", callback: "SAVE_ALL"},
      {seperator: true},
      {name: "Auto Save", isCheckable: true, callback: "TOGGLE_AUTO_SAVE"},
      {seperator: true},
      {name: "Preferences", callback: "OPEN_PREFERENCE_SETTINGS"},
      {seperator: true},
      {name: "Revert File", callback: "REVERT_FILE"},
      {name: "Close Editor", callback: "CLOSE_EDITOR"},
      {name: "Close Folder", callback: "CLOSE_FOLDER"},
      {name: "Close Window", callback: "CLOSE_WINDOW"}
    ]
  },
  {name: "Edit", submenu: [
    {name: "Word Wrap", isCheckable: true}
  ]},
  {name: "Selection"},
  {name: "View"},
  {name: "Go", submenu: [
    {name: "Share", icon: "&#xE72D;"},
    {name: "Copy"},
    {name: "Delete"},
  ]},
  {name: "Debug"},
  {name: "Tasks"},
  {name: "Help"}
]