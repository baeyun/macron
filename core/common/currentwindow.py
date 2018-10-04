from macron import *
from common import windowmanager

class CurrentWindow(NativeBridge):

  # Gets a value that indicates whether the window
  # is active
  @macronMethod
  def isActive(self):
    return self.current_window.is_active()

  # Gets a value that determines whether this element
  # has logical focus
  @macronMethod
  def isFocused(self):
    return self.current_window.is_focused()

  # Gets a value indicating whether this element has
  # keyboard focus
  @macronMethod
  def isKeyboardFocused(self):
    return self.current_window.is_keyboard_focused()

  # Gets a value indicating whether this element is
  # visible in the user interface (UI)
  @macronMethod
  def isVisible(self):
    return self.current_window.is_visible()

  # Gets or sets a window's title
  @macronMethod
  def title(self, title):
    if title != None:
      return self.current_window.title(title)
    
    return self.current_window.title()

  # Gets or sets the height of the element
  @macronMethod
  def height(self, height):
    if height != None:
      return self.current_window.height(height)
    
    return self.current_window.height()

  # Gets or sets the width of the element
  @macronMethod
  def width(self, width):
    if width != None:
      return self.current_window.width(width)
    
    return self.current_window.width()

  # Gets or sets the maximum height constraint of the
  # element
  @macronMethod
  def maxHeight(self, max_height):
    if max_height != None:
      return self.current_window.max_height(max_height)
    
    return self.current_window.max_height()

  # Gets or sets the maximum width constraint of the
  # element
  @macronMethod
  def maxWidth(self, max_width):
    if max_width != None:
      return self.current_window.max_width(max_width)
    
    return self.current_window.max_width()

  # Gets or sets the minimum height constraint of the
  # element
  @macronMethod
  def minHeight(self, min_height):
    if min_height != None:
      return self.current_window.min_height(min_height)
    
    return self.current_window.min_height()

  # Gets or sets the minimum width constraint of the
  # element
  @macronMethod
  def minWidth(self, min_width):
    if min_width != None:
      return self.current_window.min_width(min_width)
    
    return self.current_window.min_width()

  # Gets or sets the resize mode
  @macronMethod
  def resizable(self, resizable):
    if resizable != None:
      return self.current_window.resizable(resizable)
    
    return self.current_window.resizable()

  # Gets or sets a value that indicates whether a
  # window is activated when first shown
  @macronMethod
  def focusOnStartup(self, focus_on_startup):
    if focus_on_startup != None:
      return self.current_window.focus_on_startup(focus_on_startup)
    
    return self.current_window.focus_on_startup()

  # Gets or sets a value that indicates whether the
  # window has a task bar button
  @macronMethod
  def hideInTaskbar(self, hide_in_taskbar):
    if hide_in_taskbar != None:
      return self.current_window.hide_in_taskbar(hide_in_taskbar)
    
    return self.current_window.hide_in_taskbar()

  # Gets or sets the user interface (UI) visibility of
  # this element
  @macronMethod
  def hideOnStartup(self, hide_on_startup):
    if hide_on_startup != None:
      return self.current_window.hide_on_startup(hide_on_startup)
    
    return self.current_window.hide_on_startup()

  # Gets or sets the position of the window when first
  # shown
  @macronMethod
  def startupFromCenter(self, startup_from_center):
    if startup_from_center != None:
      return self.current_window.startup_from_center(startup_from_center)
    
    return self.current_window.startup_from_center()

  # Gets or sets a value that indicates whether a
  # window is restored, minimized, or maximized
  @macronMethod
  def state(self, state):
    if state != None:
      return self.current_window.state(state)
    
    return self.current_window.state()

  # Sets visibility of window's border style
  @macronMethod
  def frameless(self, frameless):
    if frameless != None:
      return self.current_window.frameless(frameless)
    
    return self.current_window.frameless()

  # Attempts to bring the window to the foreground and
  # activates it
  # Returns {Boolean} true if the Window was
  # successfully activated; otherwise, false.
  @macronMethod
  def activate(self):
    self.current_window.activate()

  # Attempts to set focus to this element.
  # Returns {Boolean} true if keyboard focus and logical
  # focus were set to this element; false if only logical
  # focus was set to this element, or if the call to this
  # method did not force the focus to change.
  @macronMethod
  def focus(self):
    self.current_window.focus()

  # Makes a window invisible. Hide() is called on a
  # window that is closing (Closing) or has been
  # closed (Closed).
  @macronMethod
  def hide(self):
    self.current_window.hide()

  # Opens a window and returns without waiting for the
  # newly opened window to close. Show() is called on
  # a window that is closing (Closing) or has been
  # closed (Closed).
  @macronMethod
  def show(self):
    self.current_window.show()

  # Manually closes a Window.
  @macronMethod
  def close(self):
    self.current_window.close()

  # Creates a duplicate / clone of the current window
  # instance.
  @macronMethod
  def clone(self):
    windowmanager.WindowManager().create(self.current_window.config)
