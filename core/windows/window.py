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

    self.window.Title = 'Macron App'
    self.window.Width = 500
    self.window.Height = 500

    # @todo

def create_window():
  def create():
    Application().Run(MacronWindow().window)
  
  thread = Thread(ThreadStart(create))
  thread.SetApartmentState(ApartmentState.STA)
  thread.Start()
  thread.Join()            

if __name__ == '__main__':
    create_window()