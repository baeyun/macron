const { Menubar, Menu } = require('../../../index') // @todo require('macron')

module.exports = new Menubar([
  Menu.MenuItem({
    label: "File",
    submenu: [
      Menu.MenuItem({
        label: "New File",
        click: function() {
          console.log(
            require('macron').Dialog.pickFile({
              title: 'Pick file', // title of 'Save File Dialog'
              read: true,
              multiselect: true,
              initialDirectory: 'C:/Users/bukharim96/Desktop/', // initial save path
              filter: [ // 'Save As' types
                ['All files', '.*'],
                ['Text', '.txt'],
                ['HTML', '.html'],
                ['JavaScript', '.js'],
                ['CSS', '.css'],
                ['Markdown', '.md']
              ]
            })
          );
        }
      }),
      Menu.MenuItem({
        label: "Open Folder",
        click: function() {
          console.log(
            require('macron').Dialog.pickDirectory({
              title: 'Pick folder', // title of 'Pick Folder Dialog'
              initialDirectory: 'C:/Users/bukharim96/Desktop/macron_tests/' // initial save path
            })
          );
        }
      }),
      Menu.MenuItem({
        label: "Save File",
        click: function() {
          console.log(
            require('macron').Dialog.saveFile({
              title: 'Save this file as:', // title of 'Pick File Dialog'
              // content: 'Some lorem...',
              name: 'test_file_01', // default name
              initialDirectory: 'C:/Users/bukharim96/Desktop/macron_tests/', // initial save path
              defaultExtension: 'txt', // default extension
              fileTypes: [ // 'Save As' types
                ['All files', '.*'],
                ['Text', '.txt'],
                ['HTML', '.html'],
                ['JavaScript', '.js'],
                ['CSS', '.css'],
                ['Markdown', '.md']
                // etc...
              ]
            })
          );
        }
      }),
      Menu.MenuItem({
        label: "New Window",
        click: function() {
          require('macron').CurrentWindow.clone()
        }
      }),
      Menu.Seperator,
      Menu.MenuItem({label: "Open File", click: function(menuitem) {
        console.log(menuitem)
      }}),
      Menu.MenuItem({label: "Open Folder", click: function() {
        console.log('callback function')
      }}),
      Menu.Seperator,
      Menu.MenuItem({label: "Open recent", submenu: [
        Menu.MenuItem({label: "./views/CodeEditor/index.js", click: function() {
          console.log('callback function')
        }}),
        Menu.MenuItem({label: "../components/windows/MenuButton", click: function() {
          console.log('callback function')
        }}),
        Menu.MenuItem({label: "./guppy/scripts/", click: function() {
          console.log('callback function')
        }}),
        Menu.MenuItem({label: "../static/img/logo.png", click: function() {
          console.log('callback function')
        }}),
        Menu.MenuItem({label: "../vsnative/", click: function() {
          console.log('callback function')
        }})
      ]}),
      Menu.Seperator,
      Menu.MenuItem({label: "Save", click: function() {
        console.log('callback function')
      }}),
      Menu.MenuItem({label: "Save As", click: function() {
        console.log('callback function')
      }}),
      Menu.MenuItem({label: "Save All", click: function() {
        console.log('callback function')
      }}),
      Menu.Seperator,
      Menu.MenuItem({label: "Auto Save", isCheckable: true, checked: true, click: function(menuitem) {
        console.log(menuitem)
      }}),
      Menu.Seperator,
      Menu.MenuItem({label: "Preferences", click: function() {
        console.log('callback function')
      }}),
      Menu.Seperator,
      Menu.MenuItem({label: "Revert File", click: function() {
        console.log('callback function')
      }}),
      Menu.MenuItem({label: "Close Editor", click: function() {
        console.log('callback function')
      }}),
      Menu.MenuItem({label: "Close Folder", click: function() {
        console.log('callback function')
      }}),
      Menu.MenuItem({label: "Close Window", click: function() {
        console.log('callback function')
      }})
    ]
  }),
  Menu.MenuItem({label: "Edit", submenu: [
    Menu.MenuItem({label: "Word Wrap", isCheckable: true, click: function(menuitem) {
      console.log(menuitem)
    }})
  ]}),
  Menu.MenuItem({label: "Selection"}),
  Menu.MenuItem({label: "View"}),
  Menu.MenuItem({label: "Go", submenu: [
    Menu.MenuItem({label: "Share", icon: "&#xE72D;"}),
    Menu.MenuItem({label: "Copy"}),
    Menu.MenuItem({label: "Delete"}),
  ]}),
  Menu.MenuItem({label: "Debug"}),
  Menu.MenuItem({label: "Tasks"}),
  Menu.MenuItem({label: "Help"})
])