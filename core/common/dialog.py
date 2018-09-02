from macron import NativeBridge

class Dialog(NativeBridge):
  
  def openFile(self):
    from tkinter import Tk, Button, messagebox
    root = Tk(screenName="Macron")
    def say_wow(): messagebox.showwarning("Macron", "This is great so far!")
    Button(root, text="Macron", command=say_wow).pack()
    root.mainloop()

  def par(self, a, b, c):
    return {"0": a, 32: b, "jay": c}
