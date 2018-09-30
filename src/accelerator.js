var commonKeyboardValues = {
  'backspace': 8,
  'tab': 9,
  'enter': 13,
  'shift': 16,
  'ctrl': 17,
  'alt': 18,
  'pause': 19,
  'break': 19,
  'caps-lock': 20,
  'escape': 27,
  'page-up': 33,
  'page-down': 34,
  'end': 35,
  'home': 36,
  'left-arrow': 37,
  'up-arrow': 38,
  'right-arrow': 39,
  'down-arrow': 40,
  'insert': 45,
  'delete': 46,
  '0': 48,
  '1': 49,
  '2': 50,
  '3': 51,
  '4': 52,
  '5': 53,
  '6': 54,
  '7': 55,
  '8': 56,
  '9': 57,
  'a': 65,
  'b': 66,
  'c': 67,
  'd': 68,
  'e': 69,
  'f': 70,
  'g': 71,
  'h': 72,
  'i': 73,
  'j': 74,
  'k': 75,
  'l': 76,
  'm': 77,
  'n': 78,
  'o': 79,
  'p': 80,
  'q': 81,
  'r': 82,
  's': 83,
  't': 84,
  'u': 85,
  'v': 86,
  'w': 87,
  'x': 88,
  'y': 89,
  'z': 90,
  'left-window-key': 91,
  'right-window-key': 92,
  'select key': 93,
  'numpad 0': 96,
  'numpad 1': 97,
  'numpad 2': 98,
  'numpad 3': 99,
  'numpad 4': 100,
  'numpad 5': 101,
  'numpad 6': 102,
  'numpad 7': 103,
  'numpad 8': 104,
  'numpad 9': 105,
  'multiply': 106,
  'add': 107,
  'subtract': 109,
  'decimal-point': 110,
  'divide':  111,
  'f1':  112,
  'f2':  113,
  'f3':  114,
  'f4':  115,
  'f5':  116,
  'f6':  117,
  'f7':  118,
  'f8':  119,
  'f9':  120,
  'f10': 121,
  'f11': 122,
  'f12': 123,
  'num-lock': 144,
  'scroll-lock': 145,
  'semi-colon': 186,
  'equal-sign': 187,
  'comma': 188,
  'dash':  189,
  'period': 190,
  'forward-slash': 191,
  'grave-accent': 192,
  'open-bracket': 219,
  'back-slash': 220,
  'close-braket': 221,
  'single-quote': 222
}

require('macron').Accelerator = {
  commandsRegistry: {
    'Ctrl+A': function() { alert('You pressed Ctrl+A') }
  },
  register: function(command, callback) {
    if (!command || !callback)
      throw new Error('Failed to register command. Make sure to define a string command and a callback function.');

    var strcommand = String(command);
    var sessionKey = {
      ctrlKey: false,
      shiftKey: false,
      altKey: false
    };

    // Has control keys
    if (strcommand.indexOf('+') > -1) {
      var parts = strcommand.split('+');
      var controllers = parts.splice(0, parts.length - 1);
      // Further space checking
      var hotkey = parts[parts.length - 1];
      
      if (controllers.indexOf('Ctrl') > -1)
          sessionKey['ctrlKey'] = true;
      if (controllers.indexOf('Shift') > -1)
          sessionKey['shiftKey'] = true;
      if (controllers.indexOf('Alt') > -1)
          sessionKey['altKey'] = true;
    }

    window.addEventListener('keydown', function(keyEvent) {
      var pass = false;

      if (keyEvent.ctrlKey && sessionKey.ctrlKey)
        pass = true;
      if (keyEvent.shiftKey && sessionKey.shiftKey)
        pass = true;
      if (keyEvent.altKey && sessionKey.ctrlKey)
        pass = true;
      
      if (pass)
        if (keyEvent.which == commonKeyboardValues[hotkey.toLowerCase()])
          callback(keyEvent);
    });

    this.commandsRegistry[command] = callback;
  }
}