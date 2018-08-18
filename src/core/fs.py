import os
import sys
import fnmatch
import webview
from pathlib import Path
from shutil import copyfile, rmtree

class FileSystem:
  def __init__(self, console):
    self.console = console
    self.window_title = "New Window"
    self.window_uid = None
  
  # Saves immediately without waiting for close
  # Ensures file is synced with latest changes
  def sync_file_updates(self, file_stream):
    file_stream.flush()
    os.fsync(file_stream.fileno())

  def inject_js(self, params):
    script = ''.join(params["script"]) or ""
    uid = ''.join(params["uid"]) or "master"

    webview.evaluate_js(script=script, uid="master")
  
  # @todo refactor naming
  def open_file_dialog(self, params):
    return
    # file_types = (
    #   'JavaScript Files (*.js;*.hc)',
    #   'All files (*.*)'
    # )

    # dt = params["dialogType"]

    # file_stream = webview.create_file_dialog(
    #   webview.OPEN_DIALOG if dt == "OPEN_FILE" else webview.SAVE_DIALOG if dt == "SAVE_FILE" else webview.FOLDER_DIALOG if dt == "OPEN_FOLDER" else None,
    #   allow_multiple=params["allowMultipleFiles"],
    #   file_types=params["fileTypes"]
    # )

    # return {
    #   "message": file_stream
    # }
  
  def write_file(self, params):
    file_path = ''.join(params["filePath"])
    file_contents = ''.join(params["content"])
    f = open(file_path, "x")
    f.write(file_contents)
    self.sync_file_updates(f)
    f.close()
    return f
  
  def read_file(self, path):
    file_path = ''.join(path)
    
    with open(file_path, "r") as f:
      return f.read()
  
  def append_file(self, params):
    file_path = ''.join(params["filePath"])
    content = ''.join(params["content"])
    
    with open(file_path, "a") as f:
      f.write(content)
      self.sync_file_updates(f)
      return f.read()
  
  def clear(self, path):
    file_path = ''.join(path)
    
    with open(file_path, "w") as f:
      try:
        f.truncate(0)
        self.sync_file_updates(f)
        return True
      except Exception as e:
        self.console.log(e)
        return False
  
  def copy_file(self, params):
    # @note 'from' is a reserved keyword
    src = ''.join(params["from"])
    to = ''.join(params["to"])
    return copyfile(src, to)
  
  def is_file(self, path):    
    return Path(''.join(path)).is_file()
  
  def is_dir(self, path):
    return Path(''.join(path)).is_dir()
  
  def mkdir(self, path):
    path = ''.join(path)

    if not self.is_dir(path):
      try:
        os.makedirs(path)
        return True
      except OSError as e:
        self.console.log(e)
        return False
  
  def chdir(self, path):
    path = ''.join(path)

    if not self.is_dir(path):
      try:
        os.chdir(path)
        return True
      except OSError as e:
        self.console.log(e)
        return False
  
  # @todo Fix minor bug
  # Unresolved issue with paths
  def realpath(self, path):
    path = Path(''.join(path))

    if path.exists():
      return path.resolve()
    return None
  
  # @note should be noted that if the files
  # are not in the working directory you will
  # need the full path.
  def rename(self, params):
    return os.rename(''.join(params["old"]), ''.join(params["new"]))
  
  # @note removes file permanently
  # @todo copy to 'Recycle Bin' or 'Trash'
  # to temporary remove
  def unlink(self, path):
    if self.is_file(path):
      os.remove(path)
    return
  
  # @note removes all directory content
  def rmdir(self, path):
    if self.is_dir(path):
      rmtree(path)
    return

  # @note os.rmdir() on Windows removes directory
  # symbolic link even if the target dir isn't empty
  def rmdir_empty(self, path):
    if self.is_dir(path):
      os.rmdir(path)
    return
  
  # @todo enhance accessability
  def read_dir(self, path):
    if self.is_dir(path):
      return os.listdir(path)
    return
  
  # @note unlike read_dir it returns a list with absolute
  # paths of files and dirs with Path(path)
  def read_dir_glob(self, params):
    ff = []

    if self.is_dir(''.join(params["path"])):
      for f in self.read_dir(''.join(params["path"])):
        if fnmatch.fnmatch(f, ''.join(params["pattern"])):
          ff.append(f)

    return ff