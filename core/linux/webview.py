import gi
import sys
import threading
from os import path

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gdk, WebKit2

dirname = path.dirname(path.realpath(__file__))

from json import dumps
from bridge import MacronBridge

from utils import get_resource_path

class MacronWebview(WebKit2.WebView):
  def __init__(self, current_window, config):
    super(WebKit2.WebView, self).__init__()

    if "devServerURI" in config and not hasattr(sys, '_MEIPASS'):
      self.load(config["devServerURI"])
    else:
      self.load(
        get_resource_path(
          'macron/app/index.html',
          'file://' + config["rootPath"] + 'public/index.html'
        )
      )

    # Load main macron JavaScript APIs
    init_scripts = r'var macron = {};'
    
    with open(
      get_resource_path(
        'macron/core/polyfills/require.js',
        dirname + '/../../src/polyfills/require.js'
      )
    ) as f: init_scripts += f.read()

    with open(
      get_resource_path(
        'macron/core/init.js',
        dirname + '/../../src/init.js'
      )
    ) as f: init_scripts += f.read()

    with open(
      get_resource_path(
        'macron/core/menu.js',
        dirname + '/../../src/menu.js'
      )
    ) as f: init_scripts += f.read()

    with open(
      get_resource_path(
        'macron/core/contextmenu.js',
        dirname + '/../../src/contextmenu.js'
      )
    ) as f: init_scripts += f.read()

    # with open(
    #   get_resource_path(
    #     'macron/core/accelerator.js',
    #     dirname + '/../../src/accelerator.js'
    #   )
    # ) as f: init_scripts += f.read()

    # execute init_scripts in current context
    self.evaluate_script(init_scripts)

    # Bridge
    MacronBridge().initialize(
      current_window=current_window,
      context=self,
      root_path=config["rootPath"],
      native_modules=config["nativeModules"]
    )

    # TODO: Add inspector. JS APIs need logging.
    # inspector = self.get_inspector()
    # inspector.connect('inspect-web-view', get_webkit_inspector)
    # inspector.attach()
    # inspector.show()

  def evaluate_script(self, script):
    self.run_javascript(script)

  def triggerEvent(self, event):
    self.evaluate_script(
      '''_macron.RegisteredEventCallbacks.{}.forEach(
        function(callback) {{
          callback()
        }}
      );'''.format(event)
    )

  # Gets the Uri of the current document hosted in the WebBrowser.
  def getSource(self):
    return self.get_uri()

  # Sets the Uri of the current document hosted in the WebBrowser.
  # @param uri {string}
  def load(self, uri):
    self.load_uri(uri)

  # Reloads the current page with optional cache validation.
  # If noCache is true, the WebBrowser control refreshes
  # without cache validation by sending a "Pragma:no-cache"
  # header to the server.
  # @param noCache {bool}
  # TODO test
  def refresh(self, noCache=False):
    if noCache:
      self.webiew.reload()
    else:
      self.webiew.reload_bypass_cache()

  # Navigate back to the previous document, if there is one.
  # TODO test
  def goBack(self):
    self.go_back()

  # Navigate forward to the next document, if there is one.
  # TODO test
  def goForward(self):
    self.go_forward()
