module.exports = [
  {
    name: "File",
    submenu: [
      {name: "New File", callback: "create_file"},
      {name: "New Window", callback: "create_window"},
      {seperator: true},
      {name: "Open File", callback: "open_file"},
      {name: "Open Folder", callback: "open_folder"},
      {seperator: true},
      {name: "Open recent", submenu: [ // @todo get from store
        {name: "./views/CodeEditor/index.js", callback: "open_recent"},
        {name: "../components/windows/MenuButton", callback: "open_recent"},
        {name: "./guppy/scripts/", callback: "openrecent"},
        {name: "../static/img/logo.png", callback: "open_recent"},
        {name: "../vsnative/", callback: "open_recent"}
      ]},
      {seperator: true},
      {name: "Save", callback: "save"},
      {name: "Save As", callback: "save_as"},
      {name: "Save All", callback: "save_all"},
      {seperator: true},
      {name: "Auto Save", toggle: true, callback: "toggle_auto_save"},
      {seperator: true},
      {name: "Preferences", callback: "open_preference_settings"},
      {seperator: true},
      {name: "Revert File", callback: "revert_file"},
      {name: "Close Editor", callback: "close_editor"},
      {name: "Close Folder", callback: "close_folder"},
      {name: "Close Window", callback: "close_window"}
    ]
  },
  {name: "Edit", submenu: [
    {name: "Word Wrap", toggle: true}
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