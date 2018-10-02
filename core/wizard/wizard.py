from tkinter import Tk, messagebox, filedialog, END, StringVar, NORMAL, DISABLED
from pygubu import Builder

class MacronSetupWizard:
  def __init__(self, root):
    self.root = root
    self.navigate('./intro-gui.ui')
    self.mainwindow = self.builder.get_object('Frame_0', root)

  def on_intro_next(self):
    self.navigate('./license-gui.ui')
    self.builder.get_object('Radiobutton_5').select()
    self.builder.get_object('Button_2').configure(state=DISABLED)
  
  def on_license_next(self):
    self.navigate('./settings-gui.ui')
    self.builder.get_object('Checkbutton_3').select()
    self.builder.get_object('Checkbutton_4').select()

  def on_settings_next(self):
    self.navigate('./download-gui.ui')
  
  def on_license_back(self):
    self.navigate('./intro-gui.ui')
  
  def on_settings_back(self):
    self.navigate('./license-gui.ui')
  
  def on_not_accept(self):
    self.builder.get_object('Button_2').configure(state=DISABLED)
  
  def on_accept(self):
    self.builder.get_object('Button_2').configure(state=NORMAL)
  
  def on_browse_dir(self):
    response = filedialog.askdirectory(
      title='Please select installation path...'
    )
    entry = self.builder.get_object('Entry_2')
    entry.delete(0, END)
    entry.insert(0, response)

  def on_finish(self):
    self.root.destroy()
  
  def on_retry_download(self):
    response = messagebox.showwarning(
      type=messagebox.YESNO,
      title='Vue CLI Setup Wizard',
      message='Are you sure you want to retry the installation process?'
    )

    if response == 'yes':
      self.root.destroy()
  
  def on_cancel(self):
    response = messagebox.showwarning(
      type=messagebox.OKCANCEL,
      title='Vue CLI Setup Wizard',
      message='Are you sure you want to cancel the installation process?'
    )

    if response == 'ok':
      self.root.destroy()

  # Helpers
  def navigate(self, next_view):
    self.builder = Builder()
    self.builder.add_from_file(next_view)
    self.mainwindow = self.builder.get_object('Frame_0', root)
    self.builder.connect_callbacks(self)

if __name__ == '__main__':
  root = Tk()
  root.title('Vue CLI Setup Wizard')
  root.geometry('500x360')

  # # Center window
  # root.update_idletasks()
  # width = root.winfo_width()
  # height = root.winfo_height()
  # x = (root.winfo_screenwidth() // 2) - (width // 2)
  # y = (root.winfo_screenheight() // 2) - (height // 2)
  # root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

  root.resizable(width=False, height=False)
  app = MacronSetupWizard(root)
  root.mainloop()
