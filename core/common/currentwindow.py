from macron import *
from common import window

class CurrentWindow(NativeBridge):

  @macronMethod
  def title(self, title):
    if title != None:
      return self.current_window.title(title)
    
    return self.current_window.title()

  @macronMethod
  def height(self, height):
    if height != None:
      return self.current_window.height(height)
    
    return self.current_window.height()

  @macronMethod
  def width(self, width):
    if width != None:
      return self.current_window.width(width)
    
    return self.current_window.width()

  @macronMethod
  def max_height(self, max_height):
    if max_height != None:
      return self.current_window.max_height(max_height)
    
    return self.current_window.max_height()

  @macronMethod
  def max_width(self, max_width):
    if max_width != None:
      return self.current_window.max_width(max_width)
    
    return self.current_window.max_width()

  @macronMethod
  def min_height(self, min_height):
    if min_height != None:
      return self.current_window.min_height(min_height)
    
    return self.current_window.min_height()

  @macronMethod
  def min_width(self, min_width):
    if min_width != None:
      return self.current_window.min_width(min_width)
    
    return self.current_window.min_width()

  @macronMethod
  def resizable(self, resizable):
    if resizable != None:
      return self.current_window.resizable(resizable)
    
    return self.current_window.resizable()

  @macronMethod
  def focus_on_startup(self, focus_on_startup):
    if focus_on_startup != None:
      return self.current_window.focus_on_startup(focus_on_startup)
    
    return self.current_window.focus_on_startup()

  @macronMethod
  def hide_in_taskbar(self, hide_in_taskbar):
    if hide_in_taskbar != None:
      return self.current_window.hide_in_taskbar(hide_in_taskbar)
    
    return self.current_window.hide_in_taskbar()

  @macronMethod
  def hide_on_startup(self, hide_on_startup):
    if hide_on_startup != None:
      return self.current_window.hide_on_startup(hide_on_startup)
    
    return self.current_window.hide_on_startup()

  @macronMethod
  def startup_from_center(self, startup_from_center):
    if startup_from_center != None:
      return self.current_window.startup_from_center(startup_from_center)
    
    return self.current_window.startup_from_center()

  @macronMethod
  def state(self, state):
    if state != None:
      return self.current_window.state(state)
    
    return self.current_window.state()

  @macronMethod
  def frameless(self, frameless):
    if frameless != None:
      return self.current_window.frameless(frameless)
    
    return self.current_window.frameless()

  @macronMethod
  def clone(self):
    win = window.Window().create(self.current_window.config)
    win.show()
    