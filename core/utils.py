import sys
from os import path

# return build / dev resource paths
def get_resource_path(build_resource_path, resource_path=None):
  try:
    return path.join(sys._MEIPASS, build_resource_path)
  except:
    return resource_path
