import sys
from os import path, startfile
from tkinter import Tk, messagebox, filedialog, END, NORMAL, DISABLED, Label
from json import load, loads
from pygubu import Builder
from urllib.request import urlopen, urlretrieve, URLError
from zipfile import ZipFile
from pythoncom import CoInitialize
from win32com.client import Dispatch
from winshell import desktop
import threading
# from PIL import ImageTk, Image

# Get current dir for loading core components
try:
  RESOURCE_PATH = path.join(sys._MEIPASS, '')
except:
  RESOURCE_PATH = path.join(path.dirname(path.realpath(__file__)), '')

sys.path.append(RESOURCE_PATH)

class MacronSetupWizard:
  def __init__(self):
    self.root = root = Tk()
    root.withdraw()
    root.title('Setup Wizard')
    root.geometry('500x360')
    root.iconbitmap(RESOURCE_PATH + 'icon.ico')

    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.deiconify()

    root.resizable(width=False, height=False)

    self.settings = {
      'app_name': 'MacronApp',
      'install_path': 'C:\Program Files', # TODO: Get default install path
      'create_shortcut': True,
      'start_after_setup': True
    }

    with open(RESOURCE_PATH + '.setupdata') as f:
      setupData = load(f)
      self.settings['app_name'] = setupData['app_name']
      self.settings['app_repo_url'] = setupData['app_repo_url']

    with open(RESOURCE_PATH + 'LICENSE') as f:
      self.settings['app_license'] = f.read()
    
    with open(RESOURCE_PATH + 'intro-view.xml') as f:
      self.navigate(f.read())
    
    self.mainwindow = self.builder.get_object('Frame_0', root)
    self.root.title(self.settings['app_name'] + ' Setup Wizard')
    self.builder.get_object('WelcomeLabel').config(text='Welcome to the {} Setup Wizard'.format(self.settings['app_name']))
    self.builder.get_object('IntroLabel').config(text='''This wizard will install {} on your computer.

It is recommended that you close all other applications before continuing.

Click Next to continue, or Cancel to exit Setup.'''.format(self.settings['app_name']))
    # self.set_image(
    #   (160, 310),
    #   self.settings['setup_banner'],
    #   self.builder.get_object('SetupBanner')
    # )

    root.mainloop()

  def on_intro_next(self):
    with open(RESOURCE_PATH + 'license-view.xml') as f:
      self.navigate(f.read())
    
    # self.set_image(
    #   (60, 60),
    #   self.settings['setup_logo'],
    #   self.builder.get_object('SetupLogo')
    # )
    self.builder.get_object('LicenseInput').delete('1.0', END)
    self.builder.get_object('LicenseInput').insert('1.0', self.settings['app_license'])
    self.builder.get_object('LicenseInput').config(state=DISABLED)
    self.builder.get_object('Radiobutton_5').select()
    self.builder.get_object('Button_2').configure(state=DISABLED)
  
  def on_license_next(self):
    with open(RESOURCE_PATH + 'settings-view.xml') as f:
      self.navigate(f.read())

    # self.set_image(
    #   (60, 60),
    #   self.settings['setup_logo'],
    #   self.builder.get_object('SetupLogo')
    # )
    self.builder.get_object('SetupReadyLabel').config(text='Setup is ready to download and install {} on your computer.'.format(self.settings['app_name']))
    self.builder.get_object('Entry_2').insert(0, self.settings['install_path'])
    self.builder.get_object('Checkbutton_3').select()
    self.builder.get_object('Checkbutton_4').select()

  def on_settings_next(self):
    self.settings['create_shortcut'] = self.builder.create_variable('boolean:create_shortcut').get()
    self.settings['start_after_setup'] = self.builder.create_variable('boolean:start_after_setup').get()
    
    with open(RESOURCE_PATH + 'download-view.xml') as f:
      self.navigate(f.read())

    # self.set_image(
    #   (60, 60),
    #   self.settings['setup_logo'],
    #   self.builder.get_object('SetupLogo')
    # )
    # self.builder.get_object('FinishButton').config(state=DISABLED)

    # self.downloadThread = threading.Thread(target=self.download)
    # self.downloadThread.start()

  def on_license_back(self):
    with open(RESOURCE_PATH + 'intro-view.xml') as f:
      self.navigate(f.read())
  
  def on_settings_back(self):
    with open(RESOURCE_PATH + 'license-view.xml') as f:
      self.navigate(f.read())
  
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
    # self.builder.get_object('DownloadStatusLabel').config(text="Obtaining latest release...")

    # try:
    #   repoURL = urlopen(self.settings['app_repo_url'] + '.setupdata')
    #   data = repoURL.read()
    #   encoding = repoURL.info().get_content_charset('utf-8')
    #   latestSetupData = loads(data.decode(encoding))
    # except:
    #   messagebox.showwarning(
    #     title='{} Setup Wizard'.format(self.settings['app_name']),
    #     message='An unexpected error occured. Setup wizard is unable to obtain additional files.'
    #   )

    #   return
    
    def reporthook(blocknum, blocksize, totalsize):
      self.builder.get_object('DownloadStatusLabel').config(text="Downloading...")
      
      readsofar = blocknum * blocksize
      if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        self.builder.create_variable('double:download_progress').set(percent)
        self.builder.get_object('DownloadRatio').config(
          # text='{:.1} %'.format(percent)
          text="{:.1f} / {:.1f} MB".format(readsofar / 1048576, totalsize / 1048576)
        )
        
        if readsofar >= totalsize: # near the end
          self.builder.get_object('DownloadStatusLabel').config(text="Download complete")
          self.builder.get_object('RetryButton').config(state=DISABLED)
      else: # total size is unknown
        pass

    # try: # download
    filehandle, _ = urlretrieve(
      # latestSetupData['latest_windows_dist_url'],
      url='https://github.com/bukharim96/macron/raw/master/playground/helloapp/dist/windows/HelloApp_0.1.0.zip',
      reporthook=reporthook
    )

    # try: # install
    self.builder.get_object('InstallStatusLabel').config(text="Installing...")
    ZipFile(filehandle).extractall(self.settings['install_path'])
    if self.settings['create_shortcut']:
      CoInitialize()
      appPath = '{}\\{}\\{}.exe'.format(self.settings['install_path'], self.settings['app_name'], self.settings['app_name'])
      self.createShortcut(
        path=os.path.join(desktop(), self.settings['app_name'].replace('_', ' ') + '.lnk'),
        target=appPath,
        wDir='{}\\{}'.format(self.settings['install_path'], self.settings['app_name']),
        icon=appPath
      )
    self.builder.get_object('InstallStatusLabel').config(text="Installation complete!")
    self.builder.get_object('FinishButton').config(state=NORMAL)
      # except:
      #   messagebox.showwarning(
      #     title='{} Setup Wizard'.format(self.settings['app_name']),
      #     message='Setup is unable to install additional files.'
      #   )
    # except:
    #   messagebox.showwarning(
    #     title='{} Setup Wizard'.format(self.settings['app_name']),
    #     message='Setup is unable to download additional files. Please make sure that you have an internet connection, then click Retry.'
    #   )
  
  def on_finish(self):
    if self.settings['start_after_setup']:
      startfile('{}\\{}\\{}.exe'.format(self.settings['install_path'], self.settings['app_name'], self.settings['app_name']))
    
    self.root.destroy()
  
  def on_retry_download(self):
    response = messagebox.showwarning(
      type=messagebox.YESNO,
      title='{} Setup Wizard'.format(self.settings['app_name']),
      message='Are you sure you want to retry downloading?'
    )

    if response == 'yes':
      self.root.destroy()
  
  def on_cancel(self):
    response = messagebox.showwarning(
      type=messagebox.OKCANCEL,
      title='{} Setup Wizard'.format(self.settings['app_name']),
      message='Are you sure you want to cancel the installation process?'
    )

    if response == 'ok':
      # if self.downloadThread: self.downloadThread._Thread_stop()
      self.root.destroy()

  # Helpers
  def navigate(self, next_view_ui):
    self.builder = Builder()
    self.builder.add_from_string(next_view_ui)
    self.mainwindow = self.builder.get_object('Frame_0', self.root)
    self.builder.connect_callbacks(self)

  # convert bytes to MB.... GB... etc...
  def human_bytes(self, num):
    step_unit = 1000.0 #1024 bad the size
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
      if num < step_unit: return "%3.1f %s" % (num, x)
      num /= step_unit

  def createShortcut(self, path, target='', wDir='', icon=''):    
    ext = path[-3:]
    if ext == 'url':
      shortcut = file(path, 'w')
      shortcut.write('[InternetShortcut]\n')
      shortcut.write('URL=%s' % target)
      shortcut.close()
    else:
      shell = Dispatch('WScript.Shell')
      shortcut = shell.CreateShortCut(path)
      shortcut.Targetpath = target
      shortcut.WorkingDirectory = wDir
      if icon == '':
        pass
      else:
        shortcut.IconLocation = icon
      shortcut.save()
  
  # def set_image(self, dimensions, img_path, frame):
  #   img = Image.open(img_path)
  #   img = ImageTk.PhotoImage(img.resize(dimensions, Image.ANTIALIAS))
  #   lb = Label(frame, image=img, bg='#ffffff')
  #   lb.image = img
  #   lb.pack()
  #   pass

if __name__ == '__main__':
  MacronSetupWizard()
