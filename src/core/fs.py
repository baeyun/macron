import os
import sys
import chalk
import webview
from os import getcwd, fsync

class FileSystem:
  def __init__(self):
    self.window_title = "New Window"
    self.window_uid = None
  
  # Saves immediately without waiting for close
  # Ensures file is synced with latest changes
  def sync_file_updates(self, file_stream):
    file_stream.flush()
    fsync(file_stream.fileno())
  
  def open_file_dialog(self):
    file_types = (
      'Image Files (*.bmp;*.jpg;*.gif)',
      'All files (*.*)'
    )
    files = webview.create_file_dialog(
      webview.OPEN_DIALOG,
      allow_multiple=True,
      file_types=file_types
    )

    return files
  
  def create_file(self, params):
    file_path = ''.join(params["filePath"])
    file_contents = ''.join(params["content"])

    if file_path and file_contents:
      f = open(file_path, 'w+')
      f.write(file_contents)
      self.sync_file_updates(f)
      f.close()