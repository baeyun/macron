import clr
import sys

if sys.platform.lower() not in ['cli','win32']:
  print("only windows is supported for wpf")
clr.AddReference(r"wpf\PresentationFramework")

from System.Windows.Markup import XamlReader
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows import Application, Window


class MacronWindow(Window):
  def __init__(self):
    self.window = Window()
    
    # if content:
    #   self.window.Content = content

    # Gets or sets a window's title
    self.window.Title = 'Macron App'
    # Gets or sets the height of the element
    self.window.Height = 500
    # Gets or sets the width of the element
    self.window.Width = 500
    # Gets or sets the maximum height constraint of the element
    # # self.window.MaxHeight = 500
    # Gets or sets the maximum width constraint of the element
    # # self.window.MaxWidth = 500
    # Gets or sets the minimum height constraint of the element
    # # self.window.MinHeight = 500
    # Gets or sets the minimum width constraint of the element
    # # self.window.MinWidth = 500
    # Gets a value that indicates whether the window is active
    # # self.window.IsActive
    # Gets a value that determines whether this element has logical focus
    # # self.window.IsFocused = True
    # Gets a value indicating whether this element has keyboard focus
    # # self.window.IsKeyboardFocused
    # Gets a value indicating whether this element is visible in the user interface (UI)
    # # self.window.IsVisible
    # Gets or sets the resize mode 
    #   Opts:
    #     - CanMinimize=1 | The user can only minimize the window and restore it from the taskbar. The Minimize and Maximize boxes are both shown, but only the Minimize box is enabled.
    #     - CanResize=2 | The user has the full ability to resize the window, using the Minimize and Maximize boxes, and a draggable outline around the window. The Minimize and Maximize boxes are shown and enabled. (Default).
    #     - CanResizeWithGrip=3 | This option has the same functionality as CanResize, but adds a "resize grip" to the lower right corner of the window.
    #     - NoResize=0 | The user cannot resize the window. The Maximize and Minimize boxes are not shown.
    # # self.window.ResizeMode = 0
    # Gets or sets a value that indicates whether a window is activated when first shown
    #   Default: True
    # # self.window.ShowActivated
    # Gets or sets a value that indicates whether the window has a task bar button
    #   Default: True
    # # self.window.ShowInTaskbar
    # Gets or sets the user interface (UI) visibility of this element
    #   Opts:
    #     - Collapsed=2	| Do not display the element, and do not reserve space for it in layout.
    #     - Hidden=1	| Do not display the element, but reserve space for the element in layout.
    #     - Visible	0	| Display the element.
    # # self.window.Visibility
    # Gets or sets the position of the window when first shown
    #   Opts:
    #     - CenterOwner=2	| The startup location of a Window is the center of the Window that owns it, as specified by the Owner property.
    #     - CenterScreen=1 | The startup location of a Window is the center of the screen that contains the mouse cursor.
    #     - Manual=0	| The startup location of a Window is set from code, or defers to the default Windows location.
    self.window.WindowStartupLocation = 1
    # Gets or sets a value that indicates whether a window is restored, minimized, or maximized
    #   Opts:
    #     - Maximized=2	| The window is maximized.
    #     - Minimized=1	| The window is minimized.
    #     - Normal=0	| The window is restored.
    # # self.window.WindowState = 2
    # Gets or sets a window's border style
    #   Opts:
    #     - None=0 | Only the client area is visible. We'll use to simulate a frameless window
    # # self.window.WindowStyle = 0

    # # def on_Activated(self, sender, args):
    # Occurs when a window becomes the foreground window.
    # # self.window.Activated += self.on_Activated
    # Occurs when the window is about to close.
    # self.window.Closed += self.on_Closed
    # Occurs directly after Close() is called, and can be handled to cancel window closure.
    # # self.window.Closing += self.on_Closing
    # Occurs just before any context menu on the element is closed.
    # # self.window.ContextMenuClosing += self.on_ContextMenuClosing
    # Occurs when any context menu on the element is opened.
    # # self.window.ContextMenuOpening += self.on_ContextMenuOpening
    # Occurs when a window becomes a background window.
    # # self.window.Deactivated += self.on_Deactivated
    # Occurs when the value of the Focusable property changes.
    # # self.window.FocusableChanged += self.on_FocusableChanged
    # Occurs when a key is pressed while focus is on this element.
    # # self.window.PreviewKeyDown += self.on_PreviewKeyDown
    # Occurs when a key is released while focus is on this element.
    # # self.window.PreviewKeyUp += self.on_PreviewKeyUp
    # Occurs when either the ActualHeight or the ActualWidth properties change value on this element.
    # # self.window.SizeChanged += self.on_SizeChanged
    # Occurs when the window's WindowState property changes.
    # # self.window.StateChanged += self.on_StateChanged

  # Attempts to bring the window to the foreground and activates it
  # Returns {Boolean} true if the Window was successfully activated;
  # otherwise, false.
  def activate():
    return self.window.Activate()

  # Attempts to set focus to this element.
  # Returns {Boolean} true if keyboard focus and logical
  # focus were set to this element; false if only logical
  # focus was set to this element, or if the call to this
  # method did not force the focus to change.
  def focus():
    return self.window.Focus()

  # Makes a window invisible. Hide() is called on a window
  # that is closing (Closing) or has been closed (Closed).
  def hide():
    self.window.Hide()

  # Opens a window and returns without waiting for the newly
  # opened window to close. Show() is called on a window that
  # is closing (Closing) or has been closed (Closed).
  def show():
    self.window.Show()

  # Manually closes a Window.
  def close():
    self.window.Close()

# @todo
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

def create_window():
  def create():
    Application().Run(MacronWindow().window)
  
  thread = Thread(ThreadStart(create))
  thread.SetApartmentState(ApartmentState.STA)
  thread.Start()
  thread.Join()            

if __name__ == '__main__':
  create_window()