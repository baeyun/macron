import sys
import clr
from os import path

dirname = path.dirname(path.realpath(__file__))
sys.path.append(path.join(dirname, 'assemblies'))
clr.AddReference("MacronInterop")

from MacronInterop import IWebviewBridge

class MacronBridge(IWebviewBridge):
  __namespace__ = 'MacronBridge'

  def eval_python(self, script):
    return eval(script)

  def call(self, className, methodName, args):
    return {}