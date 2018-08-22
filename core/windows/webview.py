import sys
import clr
from os import path

clr.AddReference(r"wpf\PresentationFramework")

sys.path.insert(0, path.dirname(path.abspath(__file__)))

from System.Windows.Controls import WebBrowser
from System.IO import StreamReader
from System.Windows.Navigation import LoadCompletedEventHandler

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
      #   self.Navigate(source.read())
    # else:
    #   # handle error

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

  # @param functionName {string}
  # @param args {object}
  # def invokeScript(self, functionName, args=None):
  #   # should not be called before the document has
  #   # finished loading
  #   if self.LoadCompleted:
  #     if args:
  #       self.InvokeScript(functionName, args)
  #     else:
  #       self.InvokeScript(functionName)

  def evaluate_script(self, script=None):
    # if not script:
    #   return
    # should not be called before the document has
    # finished loading
    def evaluate(self):
      self.Document.InvokeScript("alert")
    handler = LoadCompletedEventHandler(evaluate)
    self.LoadCompleted += handler

    print(self)

