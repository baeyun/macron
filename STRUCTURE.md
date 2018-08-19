# Proposed Project Structure

A must know for all Macron contributors.

```
core/
  win/
    window.py
    webview.py (WebBrowser)
    menubar.py
  mac/
    window.py
    webview.py (Webview)
    menubar.py
  lin/
    window.py
    webview.py (Webkit)
    menubar.py
  common/
    fs.py
    http.py
    https.py
    process.py
    events.py
    sockets.py
    console.py
    os.py
    path.py
    stream.py
  __init__.py
src/
  Window.js
  constants.js
  ...
index.js
```
