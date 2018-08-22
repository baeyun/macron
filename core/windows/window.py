import sys
import clr
from os import path

# if sys.platform.lower() not in ['cli','win32']:
#   print("Only Windows Systems is supported on WPF.")

clr.AddReference(r"wpf\PresentationFramework")

from System.Windows.Markup import XamlReader
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows import Application, Window, HorizontalAlignment, VerticalAlignment, Media
# from System.Windows.Controls import WebBrowser, WrapPanel, DockPanel, Dock, Menu, MenuItem, ToolTip

sys.path.insert(0, path.dirname(path.abspath(__file__)))
from webview import MacronWebview

class MacronWindow(Window):
  def __init__(self, config):
    webview = MacronWebview(config)

    self.Content = webview

    webview.evaluate_script("""
    var body = document.getElementsByTagName('body')[0];
    body.style.backgroundColor='#333';
    body.style.color='#ddd';
    """)

    # Gets or sets a window's title
    self.Title = config["title"]
    # Gets or sets the height of the element
    self.Height = config["height"]
    # Gets or sets the width of the element
    self.Width = config["width"]
    # Gets or sets the maximum height constraint of the element
    if "maxHeight" in config:
      self.MaxHeight = config["maxHeight"]
    # Gets or sets the maximum width constraint of the element
    if "maxWidth" in config:
      self.MaxWidth = config["maxWidth"]
    # Gets or sets the minimum height constraint of the element
    if "minHeight" in config:
      self.MinHeight = config["minHeight"]
    # Gets or sets the minimum width constraint of the element
    if "minWidth" in config:
      self.MinWidth = config["minWidth"]
    # TODO handle 
      # Gets a value that indicates whether the window is active
      # # self.IsActive
      # Gets a value that determines whether this element has logical focus
      # # self.IsFocused = True
      # Gets a value indicating whether this element has keyboard focus
      # # self.IsKeyboardFocused
      # Gets a value indicating whether this element is visible in the user interface (UI)
      # # self.IsVisible
    # Gets or sets the resize mode 
    #   Opts:
    #     - CanMinimize=1 | The user can only minimize the window and restore it from the taskbar. The Minimize and Maximize boxes are both shown, but only the Minimize box is enabled.
    #     - CanResize=2 | The user has the full ability to resize the window, using the Minimize and Maximize boxes, and a draggable outline around the window. The Minimize and Maximize boxes are shown and enabled. (Default).
    #     - CanResizeWithGrip=3 | This option has the same functionality as CanResize, but adds a "resize grip" to the lower right corner of the window.
    #     - NoResize=0 | The user cannot resize the window. The Maximize and Minimize boxes are not shown.
    if not config["resizable"]:
      self.ResizeMode = 1
    # Gets or sets a value that indicates whether a window is activated when first shown
    #   Default: True
    if not config["focusOnStartup"]:
      self.ShowActivated = False
    # Gets or sets a value that indicates whether the window has a task bar button
    #   Default: True
    if config["hideInTaskbar"]:
      self.ShowInTaskbar = False
    # Gets or sets the user interface (UI) visibility of this element
    #   Opts:
    #     - Collapsed=2	| Do not display the element, and do not reserve space for it in layout.
    #     - Hidden=1	| Do not display the element, but reserve space for the element in layout.
    #     - Visible	0	| Display the element.
    if config["hideOnStartup"]:
      self.Visibility = 1
    # Gets or sets the position of the window when first shown
    #   Opts:
    #     - CenterOwner=2	 | The startup location of a Window is the center of the Window that owns it, as specified by the Owner property.
    #     - CenterScreen=1 | The startup location of a Window is the center of the screen that contains the mouse cursor.
    #     - Manual=0	     | The startup location of a Window is set from code, or defers to the default Windows location.
    # TODO start from center of parent if present exists
    if config["startupFromCenter"]:
      self.WindowStartupLocation = 1
    # Gets or sets a value that indicates whether a window is restored, minimized, or maximized
    #   Opts:
    #     - Maximized=2	| The window is maximized.
    #     - Minimized=1	| The window is minimized.
    #     - Normal=0	  | The window is restored.
    if config["startupState"] == "maximized":
      self.WindowState = 2
    elif config["startupState"] == "minimized":
      self.WindowState = 1
    # Gets or sets a window's border style
    #   Opts:
    #     - None=0 | Only the client area is visible. We'll use to simulate a frameless window
    if config["frameless"]:
      self.WindowStyle = 0

    # # def on_Activated(self, sender, args):
    # Occurs when a window becomes the foreground window.
    # # self.Activated += self.on_Activated
    # Occurs when the window is about to close.
    # self.Closed += self.on_Closed
    # Occurs directly after Close() is called, and can be handled to cancel window closure.
    # # self.Closing += self.on_Closing
    # Occurs just before any context menu on the element is closed.
    # # self.ContextMenuClosing += self.on_ContextMenuClosing
    # Occurs when any context menu on the element is opened.
    # # self.ContextMenuOpening += self.on_ContextMenuOpening
    # Occurs when a window becomes a background window.
    # # self.Deactivated += self.on_Deactivated
    # Occurs when the value of the Focusable property changes.
    # # self.FocusableChanged += self.on_FocusableChanged
    # Occurs when a key is pressed while focus is on this element.
    # # self.PreviewKeyDown += self.on_PreviewKeyDown
    # Occurs when a key is released while focus is on this element.
    # # self.PreviewKeyUp += self.on_PreviewKeyUp
    # Occurs when either the ActualHeight or the ActualWidth properties change value on this element.
    # # self.SizeChanged += self.on_SizeChanged
    # Occurs when the window's WindowState property changes.
    # # self.StateChanged += self.on_StateChanged

  # Attempts to bring the window to the foreground and activates it
  # Returns {Boolean} true if the Window was successfully activated;
  # otherwise, false.
  def activate(self):
    return self.Activate()

  # Attempts to set focus to this element.
  # Returns {Boolean} true if keyboard focus and logical
  # focus were set to this element; false if only logical
  # focus was set to this element, or if the call to this
  # method did not force the focus to change.
  def focus(self):
    return self.Focus()

  # Makes a window invisible. Hide() is called on a window
  # that is closing (Closing) or has been closed (Closed).
  def hide(self):
    self.Hide()

  # Opens a window and returns without waiting for the newly
  # opened window to close. Show() is called on a window that
  # is closing (Closing) or has been closed (Closed).
  def show(self):
    self.Show()

  # Manually closes a Window.
  def close(self):
    self.Close()

# TODO
# Properties
#  - Window.Icon
#  - Window.Uid - Gets or sets the unique identifier
#    (for localization) for this element
#  - Window.WindowState - Gets or sets a value that indicates
#    whether a window is restored, minimized, or maximized
#  - Window.ContextMenu
#  - Window.Owner - Gets or sets the Window that owns this
#    Window
#  - Window.Parent - Gets the logical parent element of this
#    element
#  - Window.OwnedWindows - Gets a collection of windows for
#    which this window is the owner
#  - Window.Language - Gets or sets localization/globalization
#    language information that applies to an element
# Methods:
#  - Window.DragMove() - Allows a window to be dragged by a mouse
#    with its left button down over an exposed area of the window's
#    client area.
#  - Window.ShowDialog() - Opens a window and returns only when
#    the newly opened window is closed.

def create_window(config):
  def create():
    Application().Run(MacronWindow(config))
  
  thread = Thread(ThreadStart(create))
  thread.SetApartmentState(ApartmentState.STA)
  thread.Start()
  thread.Join()
