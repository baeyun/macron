from inspect import getmembers, ismethod
from os.path import basename
from platform import system

# Public bridge methods decorator
def macronMethod(method):
  def wrapper(*args, **kwargs):
    if 'register_method' in kwargs and kwargs['register_method']:
      args[0].registered_public_methods.append(method.__name__)
      return

    return method(*args, **kwargs)

  return wrapper

class NativeBridge:
  def __init__(self, window=None, context=None):
    self.window = window
    self.context = context
    self.registered_public_methods = []

    self.register_public_methods()

  def register_public_methods(self):
    private_members = [
      '__init__',
      'get_methods',
      'get_filename',
      'get_modulename',
      'get_classname',
      'generate_js_api'
    ]
    
    for member in getmembers(self, predicate=ismethod):
      if member[0] in private_members:
        continue
      
      try:
        getattr(self, member[0])(register_method=True)
      except:
        continue

  def get_methods(self):
    return self.registered_public_methods

  def get_filename(self):
    return basename(__file__)

  def get_modulename(self):
    return self.__class__.__module__

  def get_classname(self):
    return self.__class__.__name__

  def generate_js_api(self):
    class_name = self.get_classname()
    members_api = ''
    for member in self.get_methods():
      if system() == "Windows":
        members_api += '''{}: function() {{
          var args = JSON.stringify(arguments) || false;
          var output = window.external.call_module_classmethod("{}", "{}", "{}", args)
          
          try {{
            return JSON.parse(output);
          }} catch(e) {{
            return output
          }}
        }},
        '''.format(member, self.get_modulename(), class_name, member)
      else:
        members_api += '''{}: function() {{
          var output = alert(JSON.stringify(["_macronBridgeCall", "{}", "{}", "{}", arguments]))
          
          try {{
            return JSON.parse(output);
          }} catch(e) {{
            return output
          }}
        }},
        '''.format(member, self.get_modulename(), class_name, member)

    js_api = 'macron.'+class_name+' = {'+members_api+'};'

    return js_api
