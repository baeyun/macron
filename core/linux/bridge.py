class MacronBridge:
  def __init__(self, webview):
    self.webview = webview

  # def run_javascript(self, script):
  #   self.webview.run_javascript(script)
  
  def eval_python(self, script):
    return eval(script)
  