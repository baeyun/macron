from macron import *
from tkinter import messagebox

class MessageBox(NativeBridge):

  @macronMethod
  def alert(self, title, msg):
    messagebox.showinfo(title, msg)

  @macronMethod
  def warn(self, arg):
    return 546534

  @macronMethod
  def error(self):
    pass
    
  @macronMethod
  def info(self):
    pass