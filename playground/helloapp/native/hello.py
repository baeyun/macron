from macron import NativeBridge

class HellBoy(NativeBridge):
  name = "Boy Helly"

  def say_hi(self):
    return super().say_wow()

class HellDude(HellBoy):
  name = "Boy Helly"

  def say_hi(self):
    return super().say_wow()

def say_hello(one, two, three):
  return one + " :: " + two + " :: " + three