import sys
import clr
from os import path
import importlib.util
from json import loads
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

  # window.external.call("hello", "say_hello", JSON.stringify({x: "5654", foo: "5435", bar: "baz"}))
  def call(self, className, methodName, args):
    if not args:
      return getattr(
        getattr(self, className),
        methodName
      )

    args = loads(args)
    args_keys = args.keys()
    args_spread = ""
    
    for key in args_keys:
      args_spread += key + "=args[\"" + key + "\"],"
    
    return eval("getattr(getattr(self, className),methodName)(" + args_spread + ")")
