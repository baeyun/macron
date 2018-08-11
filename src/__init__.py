import sys
import os
from json import loads
import webview
import chalk
import threading

sys.path.append("./src/core")

from core import NewtronCoreAPI

def main(args):
  app_root_path = args[1]
  app_config = loads(open(app_root_path + "newtron.config.json", 'r').read())
  # app_uri = app_config["src"]["uri"]
  app_html_path = app_config["src"]["html"]
  
  # webview.create_window(app_config["name"], app_root_path + app_config["src"])
  master_uid = webview.create_window(
    app_config["name"],
    app_root_path + app_html_path,
    js_api=NewtronCoreAPI(app_root_path), # Set access for logfile
    width=500,
    height=800,
    text_select=True,
    debug=True
  )

  try:
    if webview.webview_ready():
      webview.evaluate_js(
        uid = master_uid,
        script = """
          document.body.style.backgroundColor = '#222';
          document.body.style.color = '#fff';
        """
      )
  except Exception as exception:
    print(exception)

  return 0

if __name__ == "__main__":
  t = threading.Thread(target=main(args = sys.argv))
  t.start()
