import sys
import clr
from os import path

dirname = path.dirname(path.realpath(__file__))
sys.path.append(dirname)
sys.path.append(path.join(dirname, '../'))

from System import Object
from System.Windows.Controls import WebBrowser
from System.Windows.Navigation import LoadCompletedEventHandler
from System.Windows import MessageBox

from json import dumps
from bridge import MacronBridge

from utils import get_resource_path

class MacronWebview(WebBrowser):

  def __init__(self, current_window, config):
    if "devServerURI" in config:
      self.Navigate(config["devServerURI"])
    else:
      self.Navigate(
        get_resource_path(
          'macron/app/index.html',
          path.realpath(path.join(config["rootPath"], 'public/index.html'))
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

    # TODO Expose to JS
    # Gets a value that indicates whether there is a document
    # to navigate back to.
    # # self.CanGoBack
    # Gets a value that indicates whether there is a document
    # to navigate forward to.
    # # self.CanGoForward

    # TODO Handle events
    # Occurs just before navigation to a document.
    # # self.Navigating += self.handle_events()
    # Occurs when the document being navigated to is located
    # and has started downloading.
    # # self.Navigated += self.handle_events()
    # Occurs when the document being navigated to has finished
    # downloading.

  def evaluate_script(self, script, on_ready=True):
    if not script:
      return
    
    def eval_js(sender=None, args=None):
      try:
        self.InvokeScript("eval", [script])
      except Exception as e:
        print(e)

    if on_ready:
      self.LoadCompleted += LoadCompletedEventHandler(
        eval_js
      )
    else:
      eval_js()

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
    return self.Source

  # Sets the Uri of the current document hosted in the WebBrowser.
  # @param uri {string}
  def load(self, uri):
    self.Source = uri

  # Reloads the current page with optional cache validation.
  # If noCache is true, the WebBrowser control refreshes
  # without cache validation by sending a "Pragma:no-cache"
  # header to the server.
  # @param noCache {bool}
  def refresh(self, noCache=False):
    self.Refresh(noCache)

  # Navigate back to the previous document, if there is one.
  def goBack(self):
    self.GoBack()

  # Navigate forward to the next document, if there is one.
  def goForward(self):
    self.GoForward()
