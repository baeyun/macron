// macron.ContextMenu API

require('macron').ContextMenu = {
  register: function(query, menu) {
    document.querySelector(query).addEventListener('contextmenu', function(e) {
      if (e.preventDefault != undefined)
        e.preventDefault()
      
      if (e.stopPropagation != undefined)
        e.stopPropagation()

      require('macron')._ContextMenu.spawn(
        query,
        menu
      )
    })
  }
}

// Prevent default contextmenu
window.addEventListener('load', function() {
  document.querySelector('*').addEventListener('contextmenu', function(e) {
    if (e.preventDefault != undefined)
      e.preventDefault()
    
    if (e.stopPropagation != undefined)
      e.stopPropagation()
  })
})
