from macron import NativeBridge

class Dialog(NativeBridge):

  def alert(self):
    pass

  def warn(self):
    pass

  def error(self):
    pass
    
  def info(self):
    pass
  
  def openFile(self):
    from tkinter import Tk, Button, messagebox
    root = Tk(screenName="Macron")
    def say_wow(): messagebox.showwarning("Macron", "This is great so far!")
    Button(root, text="Macron", command=say_wow).pack()
    root.mainloop()

  def openFolder(self):
    pass

  def saveFile(self):
    pass
