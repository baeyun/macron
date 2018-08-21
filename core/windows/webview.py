import sys
import clr
from os import path

clr.AddReference(r"wpf\PresentationFramework")

sys.path.insert(0, path.dirname(path.abspath(__file__)))

from System.Windows.Controls import WebBrowser
from System.IO import StreamReader

class MacronWebview(WebBrowser):
  def __init__(self, config):
    if "devServerURI" in config:
      self.Navigate(config["devServerURI"])
    elif "sourcePath" in config:
      sourcePath = (config["rootPath"] + config["sourcePath"]).replace("//", "\u005c")

      self.NavigateToStream(
        StreamReader(sourcePath).BaseStream
      )

      # File to string solution
      # sourcePath = (config["rootPath"] + config["sourcePath"]).replace("//", "\u005c")
      # with open (sourcePath, "r") as source:
      #   self.NavigateToString(source.read())
    # else:
    #   # handle error

