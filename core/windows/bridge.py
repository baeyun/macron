import sys
import clr
from os import path
import importlib.util
from json import loads

from macron import NativeBridge

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

  # window.external.call_module_func("hello", "say_hello", JSON.stringify({x: "5654", foo: "5435", bar: "baz"}))
  def call_module_func(self, module_name, func_name, args):
    mod = getattr(self, module_name)
    args_spread = ""
    
    if args:
      args = loads(args)
      args_keys = args.keys()
      
      for key in args_keys:
        args_spread += "args[\"{}\"],".format(key)

    to_exec = "self.{}.{}({})".format(
      module_name,
      func_name,
      args_spread if args_spread else ""
    )

    return eval(to_exec)

  # def call_module_classproperty(self, module_name, class_name, method_name, args):
  #   mod = getattr(self, module_name)
  #   args_spread = ""
    
  #   if args:
  #     args = loads(args)
  #     args_keys = args.keys()
      
  #     for key in args_keys:
  #       args_spread += "args[\"{}\"],".format(key)

  #   to_exec = "self.{}.{}().{}".format(
  #     module_name,
  #     class_name,
  #     method_name
  #   )

  #   return eval(to_exec)

  # window.external.call_module_classmethod("hello", "HellBoy", "say_hi", JSON.stringify({x: "John", foo: "Doe"}))
  def call_module_classmethod(self, module_name, class_name, method_name, args):
    mod = getattr(self, module_name)
    args_spread = ""

    if args:
      args = loads(args)
      args_keys = args.keys()

      for key in args_keys:
        args_spread += "args[\"{}\"],".format(key)

    class_ref = eval("self.{}.{}".format(
      module_name,
      class_name
    ))

    if NativeBridge not in class_ref.__bases__:
      raise Exception("The specified class must extend macron.NativeBridge")

    return getattr(
      class_ref(),
      method_name
    )(args) if args else getattr(
      class_ref(),
      method_name
    )()
