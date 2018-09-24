const { Menubar, Menu } = require('../../../index') // require('macron')

module.exports = new Menubar([
  {
    header: "File",
    submenu: [
      {
        header: "New File",
        click: Menu.callback(function() {
          console.log(
            require('macron').Dialog.filePicker({
              title: 'Pick file', // title of 'Save File Dialog'
              read: true,
              // allowMultiPick: true,
              initialDirectoryPath: 'C:/Users/bukharim96/Desktop/macron_tests/', // initial save path
              fileTypes: [ // 'Save As' types
                ['All files', '.*'],
                ['Text', '.txt'],
                ['HTML', '.html'],
                ['JavaScript', '.js'],
                ['CSS', '.css'],
                ['Markdown', '.md']
              ]
            })
          )
        })
      },
      {
        header: "New Window",
        click: Menu.callback(function() {
          require('macron').CurrentWindow.clone()
        })
      },
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