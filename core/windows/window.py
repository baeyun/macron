import sys
import clr
from os import path

clr.AddReference(r"wpf\PresentationFramework")
sys.path.insert(0, path.dirname(path.abspath(__file__)))

from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows import Application, Window
from System.Windows.Controls import DockPanel, Dock, Grid

import tkinter
from webview import MacronWebview
from menubar import MacronMenubar

class MacronWindow(Window):

  def __init__(self, config):
    # Single hidden tkinter instance for app
    tkinter.Tk().withdraw()

    # Initialize main window
    self.title(config["title"])
    self.height(config["height"])
    self.width(config["width"])
    if "maxHeight" in config: self.max_height(config["maxHeight"])
    if "maxWidth" in config: self.max_width(config["maxWidth"])
    if "minHeight" in config: self.min_height(config["minHeight"])
    if "minWidth" in config: self.min_width(config["minWidth"])
    self.resizable(config["resizable"])
    self.focus_on_startup(config["focusOnStartup"])
    self.hide_in_taskbar(config["hideInTaskbar"])
    self.hide_on_startup(config["hideOnStartup"])
    self.startup_from_center(config["startupFromCenter"])
    self.state(config["startupState"])
    if config["frameless"]: self.frameless(True)
    
    # Draw UI
    dock = DockPanel()
    dock.LastChildFill = True

    menu = MacronMenubar(src=config["menu"]).get_menu()
    dock.SetDock(menu, Dock.Top)

    grid = Grid()
    grid.ShowGridLines = False
    
    self.webview = MacronWebview(current_window=self, config=config)
    grid.Children.Add(self.webview)
    
    dock.Children.Add(menu)
    dock.Children.Add(grid)
    self.Content = dock

    # Delegate events
    self.Activated += self.on_activated
    self.Closed += self.on_closed
    self.Closing += self.on_closing
    self.ContextMenuClosing += self.on_contextmenuclosing
    self.ContextMenuOpening += self.on_contextmenuopening
    self.Deactivated += self.on_deactivated
    self.FocusableChanged += self.on_focusablechanged
    self.PreviewKeyDown += self.on_previewkeydown
    self.PreviewKeyUp += self.on_previewkeyup
    self.SizeChanged += self.on_sizechanged
    self.StateChanged += self.on_statechanged

  # Gets a value that indicates whether the window is active
  def is_active(self):
    return self.IsActive

  # Gets a value that determines whether this element has logical focus
  def is_focused(self):
    return self.IsFocused

  # Gets a value indicating whether this element has keyboard focus
  def is_keyboard_focused(self):
    return self.IsKeyboardFocused

  # Gets a value indicating whether this element is visible in the user interface (UI)
  def is_visible(self):
    return self.IsVisible

  # Gets or sets a window's title
  def title(self, title):
    if title:
      self.Title = title
    
    return self.Title

  # Gets or sets the height of the element
  def height(self, height):
    if height:
      self.Height = height
    
    return self.Height

  # Gets or sets the width of the element
  def width(self, width):
    if width:
      self.Width = width
    
    return self.Width

  # Gets or sets the maximum height constraint of the element
  def max_height(self, max_height):
    if max_height:
      self.MaxHeight = max_height

    return self.MaxHeight

  # Gets or sets the maximum width constraint of the element
  def max_width(self, max_width):
    if max_width:
      self.MaxWidth = max_width

    return self.MaxWidth

  # Gets or sets the minimum height constraint of the element
  def min_height(self, min_height):
    if min_height:
      self.MinHeight = min_height

    return self.MinHeight

  # Gets or sets the minimum width constraint of the element
  def min_width(self, min_width):
    if min_width:
      self.MinWidth = min_width

    return self.MinWidth

  # Gets or sets the resize mode 
  #   Opts:
  #     - CanMinimize=1 | The user can only minimize the window and restore it from the taskbar. The Minimize and Maximize boxes are both shown, but only the Minimize box is enabled.
  #     - CanResize=2 | The user has the full ability to resize the window, using the Minimize and Maximize boxes, and a draggable outline around the window. The Minimize and Maximize boxes are shown and enabled. (Default).
  #     - CanResizeWithGrip=3 | This option has the same functionality as CanResize, but adds a "resize grip" to the lower right corner of the window.
  #     - NoResize=0 | The user cannot resize the window. The Maximize and Minimize boxes are not shown.
  def resizable(self, resizable):
    if resizable:
      self.ResizeMode = 2
    else:
      self.ResizeMode = 1
    
    return True if self.ResizeMode == 2 else False

  # Gets or sets a value that indicates whether a window is activated when first shown
  #   Default: True
  def focus_on_startup(self, focus_on_startup):
    if focus_on_startup:
      self.ShowActivated = focus_on_startup
    
    return self.ShowActivated

  # Gets or sets a value that indicates whether the window has a task bar button
  #   Default: True
  def hide_in_taskbar(self, hide_in_taskbar):
    if hide_in_taskbar:
      self.ShowInTaskbar = hide_in_taskbar
    
    return self.Title

  # Gets or sets the user interface (UI) visibility of this element
  #   Opts:
  #     - Collapsed=2	| Do not display the element, and do not reserve space for it in layout.
  #     - Hidden=1	| Do not display the element, but reserve space for the element in layout.
  #     - Visible	0	| Display the element.
  def hide_on_startup(self, hide_on_startup):
    if hide_on_startup:
      self.Visibility = 1
    else:
      self.Visibility = 0
    
    return True if self.Visibility else False

  # Gets or sets the position of the window when first shown
  #   Opts:
  #     - CenterOwner=2	 | The startup location of a Window is the center of the Window that owns it, as specified by the Owner property.
  #     - CenterScreen=1 | The startup location of a Window is the center of the screen that contains the mouse cursor.
  #     - Manual=0	     | The startup location of a Window is set from code, or defers to the default Windows location.
  # TODO start from center of parent if present exists
  def startup_from_center(self, startup_from_center):
    if startup_from_center:
      self.WindowStartupLocation = 1
    
    return True if self.WindowStartupLocation == 1 else False

  # Gets or sets a value that indicates whether a window is restored, minimized, or maximized
  #   Opts:
  #     - Maximized=2	| The window is maximized.
  #     - Minimized=1	| The window is minimized.
  #     - Normal=0	  | The window is restored.
  def state(self, state):
    if state == "maximized":
      self.WindowState = 2
    elif state == "minimized":
      self.WindowState = 1
    elif state == "normal":
      self.WindowState = 0
    
    if self.WindowState == 2:
      return "maximized"
    elif self.WindowState == 1:
      return "minimized"
    elif self.WindowState == 0:
      return "normal"

  # Gets or sets a window's border style
  #   Opts:
  #     - None=0 | Only the client area is visible. We'll use to simulate a frameless window
  #     - SingleBorderWindow=1 | A window with a single border. (Default)
  def frameless(self, frameless):
    if frameless:
      self.WindowStyle = 0
      # self.AllowsTransparency = True
    else:
      self.WindowStyle = 1
      # self.AllowsTransparency = False
    
    return True if self.WindowStyle == 0 else False

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

  """"""""""""""""""""""" Events """""""""""""""""""""""

  # Occurs when a window becomes the foreground window.
  def on_activated(self, sender, args):
    self.webview.triggerEvent('activate')

  # Occurs when the window is about to close.
  def on_closed(self, sender, args):
    self.webview.triggerEvent('close')

  # Occurs directly after Close() is called, and can be handled to cancel window closure.
  def on_closing(self, sender, args):
    self.webview.triggerEvent('closing')

  # Occurs just before any context menu on the element is closed.
  def on_contextmenuclosing(self, sender, args):
    self.webview.triggerEvent('contextMenuClose')

  # Occurs when any context menu on the element is opened.
  def on_contextmenuopening(self, sender, args):
    self.webview.triggerEvent('contextMenuOpen')

  # Occurs when a window becomes a background window.
  def on_deactivated(self, sender, args):
    self.webview.triggerEvent('deactivate')

  # Occurs when the value of the Focusable property changes.
  def on_focusablechanged(self, sender, args):
    self.webview.triggerEvent('focusChange')

  # Occurs when a key is pressed while focus is on this element.
  def on_previewkeydown(self, sender, args):
    self.webview.triggerEvent('keydown')

  # Occurs when a key is released while focus is on this element.
  def on_previewkeyup(self, sender, args):
    self.webview.triggerEvent('keyup')

  # Occurs when either the ActualHeight or the ActualWidth properties change value on this element.
  def on_sizechanged(self, sender, args):
    self.webview.triggerEvent('sizeChange')

  # Occurs when the window's WindowState property changes.
  def on_statechanged(self, sender, args):
    self.webview.triggerEvent('stateChange')

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
