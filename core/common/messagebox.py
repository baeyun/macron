from macron import NativeBridge

from tkinter import messagebox

class MessageBox(NativeBridge):

  def alert(self, title, msg):
    messagebox.showinfo(title, msg)

  def warn(self):
    pass

  def error(self):
    pass
    
  def info(self):
    pass