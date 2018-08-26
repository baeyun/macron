from macron import NativeBridge

class HellBoy(NativeBridge):
  name = "Boy Helly"

  def say_hi(self):
    return "Hi, all!"

  def close(self):
    self.window.close()

class HellDude(HellBoy):
  name = "Boy Helly"

  def say_hi(self):
    return "Hiiiii!"

def say_hello(one, two, three):
  return one + " :: " + two + " :: " + three