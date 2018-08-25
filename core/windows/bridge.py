import sys
import clr
from os import path
import importlib.util
# foo.MyClass()

dirname = path.dirname(path.realpath(__file__))
sys.path.append(path.join(dirname, 'assemblies'))
clr.AddReference("MacronWebviewInterop")

from MacronWebviewInterop import IMacronBridge

class MacronBridge(IMacronBridge):
  __namespace__ = 'MacronBridge'

  def init_native_modules(self, root_path, native_modules_path, native_modules):
    native_mods_root_path = (root_path + native_modules_path).replace("//", "\u005c")
    
    for modname in native_modules:
      modname = modname.split(".")[0]
      spec = importlib.util.spec_from_file_location(modname, native_mods_root_path + modname + ".py")
      setattr(self, modname, importlib.util.module_from_spec(spec))
      spec.loader.exec_module(getattr(self, modname))
   
    return self

  def eval_python(self, script):
    return eval(script)

  def call(self, className, methodName, args):
    return getattr(
      getattr(self, className),
      methodName
    )()
