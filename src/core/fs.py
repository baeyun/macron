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

  def inject_js(self, params):
    script = ''.join(params["script"]) or ""
    uid = ''.join(params["uid"]) or "master"

    webview.evaluate_js(script=script, uid="master")
  
  def open_file_dialog(self, params):
    file_types = (
      'JavaScript Files (*.js;*.hc)',
      'All files (*.*)'
    )

    dt = params["dialogType"]

    file_stream = webview.create_file_dialog(
      webview.OPEN_DIALOG if dt == "OPEN_FILE" else webview.SAVE_DIALOG if dt == "SAVE_FILE" else webview.FOLDER_DIALOG if dt == "OPEN_FOLDER" else None,
      allow_multiple=params["allowMultipleFiles"],
      file_types=params["fileTypes"]
    )

    return {
      "message": file_stream
    }
  
  def write_file(self, params):
    file_path = ''.join(params["filePath"])
    file_contents = ''.join(params["content"])

    f = open(file_path, "x")
    f.write(file_contents)
    self.sync_file_updates(f)
    f.close()

    return f