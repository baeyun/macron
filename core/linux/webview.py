import gi
import sys
import threading

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gdk, WebKit2

class MacronWebview:
  def __init__(self, config):
    self.webview = WebKit2.WebView()

    # Set development URI if not in production
    self.webview.load_uri("file:///home/bukharim96/Desktop/Projects/macron/playground/helloapp/public/index.html")
    
    # TODO: Add inspector. JS APIs need logging.
    # inspector = self.webview.get_inspector()
    # inspector.connect('inspect-web-view', get_webkit_inspector)
    # inspector.attach()
    # inspector.show()