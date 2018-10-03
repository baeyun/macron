from tkinter import Tk, messagebox, filedialog, END, NORMAL, DISABLED, Label
from pygubu import Builder
from PIL import ImageTk, Image
import threading

class MacronSetupWizard:
  def __init__(self, root):
    self.root = root
    self.navigate('./intro-gui.ui')
    self.mainwindow = self.builder.get_object('Frame_0', root)
    self.settings = {
      'install_path': 'C:/Users/default/Program Files/', # TODO: Get default install path
      'create_shortcut': True,
      'start_after_setup': True,
      'app_name': 'MacronApp',
      'setup_banner': 'setup-banner.png',
      'setup_logo': 'rx_logo60x60.png',
      'app_license': 'MIT License',
      'build_info_src': 'http://localhost:3000/releases/app/latest.txt',
      'build_info': {
        'download_size': 101.7
      }
    }
    self.root.title(self.settings['app_name'] + ' Setup Wizard')
    self.builder.get_object('WelcomeLabel').config(text='Welcome to the {} Setup Wizard'.format(self.settings['app_name']))
    self.builder.get_object('IntroLabel').config(text='''This wizard will install {} on your computer.

It is recommended that you close all other applications before continuing.

Click Next to continue, or Cancel to exit Setup.'''.format(self.settings['app_name']))
    self.set_image(
      (160, 310),
      self.settings['setup_banner'],
      self.builder.get_object('SetupBanner')
    )

  def on_intro_next(self):
    self.navigate('./license-gui.ui')
    self.set_image(
      (60, 60),
      self.settings['setup_logo'],
      self.builder.get_object('SetupLogo')
    )
    self.builder.get_object('LicenseInput').delete('1.0', END)
    self.builder.get_object('LicenseInput').insert('1.0', self.settings['app_license'])
    self.builder.get_object('LicenseInput').config(state=DISABLED)
    self.builder.get_object('Radiobutton_5').select()
    self.builder.get_object('Button_2').configure(state=DISABLED)
  
  def on_license_next(self):
    self.navigate('./settings-gui.ui')
    self.set_image(
      (60, 60),
      self.settings['setup_logo'],
      self.builder.get_object('SetupLogo')
    )
    self.builder.get_object('SetupReadyLabel').config(text='Setup is ready to download and install {} on your computer.'.format(self.settings['app_name']))
    self.builder.get_object('Entry_2').insert(0, self.settings['install_path'])
    self.builder.get_object('Checkbutton_3').select()
    self.builder.get_object('Checkbutton_4').select()

  def on_settings_next(self):
    self.settings['create_shortcut'] = self.builder.create_variable('boolean:create_shortcut').get()
    self.settings['start_after_setup'] = self.builder.create_variable('boolean:start_after_setup').get()
    self.navigate('./download-gui.ui')
    self.set_image(
      (60, 60),
      self.settings['setup_logo'],
      self.builder.get_object('SetupLogo')
    )
    self.builder.get_object('FinishButton').config(state=DISABLED)

    self.counter = 1
    
    t = threading.Timer(.05, self.download)
    t.start()

    if self.counter > 100:
      t.cancel()

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
    self.settings['install_path'] = response
    entry = self.builder.get_object('Entry_2')
    entry.delete(0, END)
    entry.insert(0, response)
  
  def download(self):
    if self.counter < 100:
      threading.Timer(.05, self.download).start()
      self.counter += 1
    else:
      self.builder.get_object('FinishButton').config(state=NORMAL)
    
    self.builder.create_variable('double:download_progress').set(self.counter)
    
    self.builder.get_object('DownloadRatio').config(
      text='{:.1f} / {:.1f} MB'.format(
        self.counter * self.settings['build_info']['download_size'] / 100,
        self.settings['build_info']['download_size']
      )
    )
  
  def on_finish(self):
    print('install_path: ' + self.settings['install_path'])
    print('create_shortcut: ' + str(self.settings['create_shortcut']))
    print('start_after_setup: ' + str(self.settings['start_after_setup']))
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
  
  def set_image(self, dimensions, img_path, frame):
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img.resize(dimensions, Image.ANTIALIAS))
    lb = Label(frame, image=img)
    lb.image = img
    lb.pack()

if __name__ == '__main__':
  root = Tk()
  root.withdraw()
  root.title('Setup Wizard')
  root.geometry('500x360')

  # # Center window
  root.update_idletasks()
  width = root.winfo_width()
  height = root.winfo_height()
  x = (root.winfo_screenwidth() // 2) - (width // 2)
  y = (root.winfo_screenheight() // 2) - (height // 2)
  root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  root.deiconify()

  root.resizable(width=False, height=False)
  app = MacronSetupWizard(root)
  root.mainloop()
