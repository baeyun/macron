import sys
import clr
from os import path

dirname = path.dirname(path.realpath(__file__))
sys.path.insert(0, dirname)

from System import Object
from System.Windows.Controls import WebBrowser
from System.IO import StreamReader
from System.Windows.Navigation import LoadCompletedEventHandler
from System.Windows import MessageBox

from json import dumps
from bridge import MacronBridge

class MacronWebview(WebBrowser):

  def __init__(self, current_window, config):
    if "devServerURI" in config:
      self.Navigate(config["devServerURI"])
    elif "sourcePath" in config:
      sourcePath = (config["rootPath"] + config["sourcePath"]).replace("//", "\u005c")

      self.NavigateToStream(
        StreamReader(sourcePath).BaseStream
      )

      # # File to string solution
      # sourcePath = (config["rootPath"] + config["sourcePath"]).replace("//", "\u005c")
      
      # with open (sourcePath, "r") as source:
      #   self.Navigate("about:blank")
      #   self.Document.OpenNew(True).Write("source.read()")
      #   self.Dock = DockStyle.Fill
    # else:
    #   # handle error

    # Load main macron JavaScript APIs
    self.evaluate_script(r'var macron = {};')
    
    with open('../../src/polyfills/require.js') as f:
      self.evaluate_script(f.read())

    with open('../../src/init.js') as f:
      self.evaluate_script(f.read())

    with open('../../src/menu.js') as f:
      self.evaluate_script(f.read())

    with open('../../src/contextmenu.js') as f:
      self.evaluate_script(f.read())
    
    # with open('../../src/accelerator.js') as f:
    #   self.evaluate_script(f.read())

    # Bridge
    MacronBridge().initialize(
      current_window=current_window,
      context=self,
      root_path=config["rootPath"],
      native_modules_path=config["nativeModulesPath"],
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
