import gi
import sys
import threading

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gdk, WebKit2

class MacronWebview:
  def __init__(self, config):
    # Dummy window
    # self.window = Gtk.Window(
    #   title="Linux (Ubuntu) WebView env",
    #   default_height=500,
    #   default_width=500
    # )
    # self.window.fullscreen()
    # self.window.connect("destroy", Gtk.main_quit)

    # Initialize Webki 2's instance of WebView
    self.webview = WebKit2.WebView()

    # Set development URI if not in production
    self.webview.load_uri("file:///home/bukharim96/Desktop/Projects/macron/playground/helloapp/public/index.html")

    # self.webview.get_inspector()
    self.inspector = self.webview.get_inspector()
    # self.inspector.connect("inspect-web-view", lambda x: self.inspector.show())

    self.webview.get_settings().set_allow_modal_dialogs(True)
    self.webview.get_settings().set_auto_load_images(True)
    self.webview.get_settings().set_default_charset("utf-8")
    # self.webview.get_settings().set_enable_caret_browsing(True)  
    self.webview.get_settings().set_enable_dns_prefetching(True)    
    self.webview.get_settings().set_enable_frame_flattening(True)    
    self.webview.get_settings().set_enable_fullscreen(True)         
    self.webview.get_settings().set_enable_html5_database(True)     
    self.webview.get_settings().set_enable_html5_local_storage(True)
    # self.webview.get_settings().set_enable_hyperlink_auditing(True)
    self.webview.get_settings().set_enable_java(True)
    self.webview.get_settings().set_enable_javascript(True)
    self.webview.get_settings().set_enable_media_stream(True)
    self.webview.get_settings().set_enable_mediasource(True)
    self.webview.get_settings().set_enable_offline_web_application_cache(True)
    self.webview.get_settings().set_enable_page_cache(True)
    self.webview.get_settings().set_enable_plugins(True)    
    self.webview.get_settings().set_enable_private_browsing(True)
    self.webview.get_settings().set_enable_resizable_text_areas(True)
    # self.webview.get_settings().set_enable_site_specific_quirks(True)
    self.webview.get_settings().set_enable_smooth_scrolling(True)
    self.webview.get_settings().set_enable_spatial_navigation(True)
    self.webview.get_settings().set_enable_tabs_to_links(True)
    self.webview.get_settings().set_enable_webaudio(True)
    self.webview.get_settings().set_enable_webgl(True)
    self.webview.get_settings().set_enable_write_console_messages_to_stdout(True)

    # self.window.add(self.webview)
  
  # def navigate(self, view, frame, request, action, decision):
  #   decision.ignore()

# def create_webview(config):
  # def create():
    # MacronWebview(config=config).window.show_all()
  
  # thread = threading.Thread(target=create)
  # thread.daemon = True
  # thread.start()
  # create()
  # Gtk.main()

# if __name__ == "__main__":
#   create_webview("No webview config for now!!!")
