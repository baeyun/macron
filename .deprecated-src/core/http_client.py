# from http.client import HTTPConnection
import http.client

class HttpClient:
  def __init__(self, console):
    self.console = console
    self.connection = None
  
  def create_server(self, params):
    # self.connection = http.client.HTTPConnection(
    #   ''.join(params["ip"]),
    #   params["port"]
    # )

    # return self.connection
    self.console.log(self.connection)
  
  def request(self, params):
    self.connection.request(
      ''.join(params["method"]),
      ''.join(params["path"]),
      ''.join(params["body"])
    )

    return self.connection.getresponse()
  
  def close(self):
    self.connection.close()