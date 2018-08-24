import sys
import clr
from os import path

clr.AddReference(r"wpf\PresentationFramework")

sys.path.insert(0, path.dirname(path.abspath(__file__)))

# from System.Windows.Forms import WebBrowser, DockStyle
from System import Object
from System.Windows.Controls import WebBrowser
from System.IO import StreamReader
from System.Windows.Navigation import LoadCompletedEventHandler
from System.Windows import MessageBox

sys.path.insert(0, path.dirname(path.abspath(__file__)))

from bridge import MacronBridge

class MacronWebview(WebBrowser):

  def __init__(self, config):
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

    # Bridge
    self.ObjectForScripting = MacronBridge()

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
    # # self.LoadCompleted += self.handle_events()

  def evaluate_script(self, script):
    if not script:
      return
    
    def eval_js(sender, args):
      try:
        self.InvokeScript("eval", [script])
      except Exception as e:
        print(e)

    self.LoadCompleted += LoadCompletedEventHandler(
      eval_js
    )


  # Gets the Uri of the current document hosted in the WebBrowser.
  def getSource(self):
    return self.Source

  # Sets the Uri of the current document hosted in the WebBrowser.
  # @param uri {string}
  def setSource(self, uri):
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