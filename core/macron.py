from inspect import getmembers, ismethod
from os.path import basename

class NativeBridge:
  def __init__(self, window=None, context=None):
    self.window = window
    self.context = context

  def get_methods(self):
    names = []
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
      
      names.append(member[0])

    return names

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

    js_api = 'macron.'+class_name+' = {'+members_api+'};'

    return js_api
