import sys
from os import path
import importlib.util
from json import loads, dumps

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2

from macron import NativeBridge

dirname = path.dirname(path.realpath(__file__))
sys.path.append(path.normpath(path.join(dirname, '../common/')))

class MacronBridge:
  
  def initialize(self, window, context, root_path, native_modules_path, native_modules):
    self.window = window
    self.context = context

    self.load_common_modules([
      'Archive',
      # 'Dialog',
      'FS',
      # 'MessageBox',
      'System'
    ])

    native_mods_root_path = (root_path + native_modules_path).replace("//", "\u005c")
    generated_js_apis = ''

    for class_name in native_modules:
      modname = class_name.lower()
      spec = importlib.util.spec_from_file_location(modname, native_mods_root_path + modname + ".py")
      setattr(self, modname, importlib.util.module_from_spec(spec))
      module = getattr(self, modname)
      spec.loader.exec_module(module)

      generated_js_apis += getattr(module, class_name)().generate_js_api()

    self.context.evaluate_script(
      generated_js_apis
    )

    self.context.connect('script-dialog', self.on_js_call)

  def on_js_call(self, web_view, dialog):
    args = loads(dialog.get_message())
    
    if '_macronBridgeCall' in args and dialog.get_dialog_type() == WebKit2.ScriptDialogType.ALERT:
      web_view.evaluate_script(
        'console.log("{}")'.format(
          self.call_module_classmethod(
            module_name=args[1],
            class_name=args[2],
            method_name=args[3],
            args=args[4]
          )
        )
      )
    
      return True

  def load_common_modules(self, class_names):
    generated_js_apis = ''

    for class_name in class_names:
      mod_name = class_name.lower()
      setattr(self, mod_name, __import__(mod_name))

      generated_js_apis += getattr(getattr(self, mod_name), class_name)().generate_js_api()

    self.context.evaluate_script(
      generated_js_apis
    )

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
      
    # print(dir(class_ref))

    output = eval("""getattr(
      class_ref(window=self.window, context=self.context),
      method_name
    )({})""".format(args_spread))

    if type(output) == list or type(output) == tuple or type(output) == dict:
      return dumps(output)
    else:
      return output
  