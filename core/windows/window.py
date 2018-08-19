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
    # Gets or sets a value indicating whether this element is enabled in the user interface (UI)
    # # self.window.IsEnabled = True
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


    # @todo
    # - Window.Icon
    # - Window.Uid - Gets or sets the unique identifier (for localization) for this element
    # - Window.WindowState - Gets or sets a value that indicates whether a window is restored, minimized, or maximized
    # - Window.ContextMenu
    # - Window.Owner - Gets or sets the Window that owns this Window
    # - Window.Parent - Gets the logical parent element of this element
    # - Window.OwnedWindows - Gets a collection of windows for which this window is the owner
    # - Window.Language - Gets or sets localization/globalization
    #   language information that applies to an element

def create_window():
  def create():
    Application().Run(MacronWindow().window)
  
  thread = Thread(ThreadStart(create))
  thread.SetApartmentState(ApartmentState.STA)
  thread.Start()
  thread.Join()            

if __name__ == '__main__':
  create_window()