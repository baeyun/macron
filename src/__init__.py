import sys
import os
from json import loads
import webview
import time
import chalk
import threading
from pathlib import Path

sys.path.append("./src")

from core import NewtronCoreAPI

def main(args):
  app_config_path = args[1]
  app_config = loads(open(app_config_path + "newtron.config.json", 'r').read())
  # app_uri = app_config["src"]["uri"]
  app_html_path = app_config["src"]["html"]

  # Create logfile
  logfile_stream = init_logfile(app_config_path)
  
  # webview.create_window(app_config["name"], app_config_path + app_config["src"])
  master_uid = webview.create_window(
    app_config["name"],
    app_config_path + app_html_path,
    js_api=NewtronCoreAPI(logfile_stream=logfile_stream), # Set access for logfile
    min_size=(500,1000),
    text_select=True,
    debug=True
  )

  # try:
  #   if webview.webview_ready():
  #     webview.evaluate_js(
  #       uid = master_uid,
  #       script = """
  #         alert('Hello');
  #       """
  #     )
  # except Exception as exception:
  #   print(exception)

  return 0

def init_logfile(path):
  logfile_path = Path(path + "newtron-debug.log")

  if logfile_path.is_file():
    f = open(logfile_path, "a")
    f.truncate(0)
    return f

  return open(logfile_path, "a")


if __name__ == "__main__":
  t = threading.Thread(target=main(args = sys.argv))
  t.start()
