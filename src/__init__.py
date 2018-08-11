import sys
import os
from json import loads
import webview
import chalk
import threading

# Get current dir
dirname = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dirname, 'core'))

from core import MacronCoreAPI

def main(args):
  app_config = loads(loads(args[1]))
  # Windows compliant path
  app_root_path = app_config["appRootPath"].replace("//", "\u005c")
  app_html_path = app_config["src"]["html"]
  # app_dev_uri = app_config["src"]["uri"]

  master_uid = webview.create_window(
    app_config["name"],
    app_root_path + app_html_path,
    js_api=MacronCoreAPI(app_root_path), # Set access for logfile
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
