import sys
import clr
from os import path

dirname = path.dirname(path.realpath(__file__))
sys.path.append(path.join(dirname, 'assemblies'))
clr.AddReference("MacronWebviewInterop")

from MacronWebviewInterop import IMacronBridge

class MacronBridge(IMacronBridge):
  __namespace__ = 'MacronBridge'

  def eval_python(self, script):
    return eval(script)

  def call(self, className, methodName, args):
    return {}