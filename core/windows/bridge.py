import sys
import clr
from os import path
# import importlib.util
from json import loads, dumps

from macron import NativeBridge

dirname = path.dirname(path.realpath(__file__))

sys.path.append(path.normpath(path.join(dirname, '../common/')))

if hasattr(sys, '_MEIPASS'):
  clr.AddReference("macron/assemblies/MacronWebviewInterop")
else:
  sys.path.append(path.join(dirname, 'assemblies'))
  clr.AddReference("MacronWebviewInterop")

from MacronWebviewInterop import IMacronBridge

class MacronBridge(IMacronBridge):
  __namespace__ = 'MacronBridge'

  def initialize(self, current_window, context, root_path, native_modules):
    self.current_window = current_window
    self.context = context

    self.load_common_modules([
      '_ContextMenu',
      'Archive',
      'CurrentWindow',
      'Dialog',
      'FileSystem',
      # 'MessageBox',
      'System',
      'WindowManager'
    ])

    self.context.ObjectForScripting = self

    # # TODO Add support in later version
    # native_mods_root_path = (root_path + native_modules_path).replace("//", "\u005c")
    # generated_js_apis = ''
    # for class_name in native_modules:
    #   modname = class_name.lower()
      # spec = importlib.util.spec_from_file_location(modname, native_mods_root_path + modname + ".py")
      # setattr(self, modname, importlib.util.module_from_spec(spec))
    #   module = getattr(self, modname)
    #   spec.loader.exec_module(module)

    #   generated_js_apis += getattr(module, class_name)().generate_js_api()

    # self.context.evaluate_script(
    #   generated_js_apis
    # )

  def load_common_modules(self, class_names):
    generated_js_apis = ''

    for class_name in class_names:
      mod_name = class_name.lower()
      setattr(self, mod_name, __import__(mod_name))

      generated_js_apis += getattr(getattr(self, mod_name), class_name)().generate_js_api()

    self.context.evaluate_script(
      generated_js_apis
    )

  def eval_python(self, script):
    return eval(script)

  # window.external.call_common_module_classmethod("system", "System", "get_platform", false)
  # TODO pre-import all common mods
  def call_common_module_classmethod(self, module_name, class_name, method_name, args):
    mod = __import__(module_name)
    class_ref = getattr(mod, class_name)
    args_spread = ""

    if args:
      args = loads(args)
      args_keys = args.keys()

      for key in args_keys:
        args_spread += "args[\"{}\"],".format(key)

    if NativeBridge not in class_ref.__bases__:
      raise Exception("The specified class must extend macron.NativeBridge")

    return eval("""getattr(
      class_ref(),
      method_name
    )({})""".format(args_spread))

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
      args_spread
    )

    return eval(to_exec)

  def call_module_classproperty(self, module_name, class_name, property_name, args):
    mod = getattr(self, module_name)
    args_spread = ""
    
    if args:
      args = loads(args)
      args_keys = args.keys()
      
      for key in args_keys:
        args_spread += "args[\"{}\"],".format(key)

    to_exec = "self.{}.{}().{}".format(
      module_name,
      class_name,
      property_name
    )

    return eval(to_exec)

  # window.external.call_module_classmethod("hello", "HellBoy", "get_methods")
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

    output = eval("""getattr(
      class_ref(current_window=self.current_window, context=self.context),
      method_name
    )({})""".format(args_spread))

    if type(output) == list or type(output) == tuple or type(output) == dict:
      return dumps(output)
    else:
      return output
