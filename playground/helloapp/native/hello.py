from macron import NativeBridge

class HellBoy(NativeBridge):
  name = "Boy Helly"

  def say_hi(self):
    # return "Hi, all!"
    from tkinter import Tk
    Tk(screenName="WOOOW! TKINTER!").mainloop()

  def close(self):
    self.window.close()

class HellDude(HellBoy):
  name = "Boy Helly"

  def say_hi(self):
    return "Hiiiii!"

def say_hello(one, two, three):
  return one + " :: " + two + " :: " + three