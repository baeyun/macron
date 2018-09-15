from macron import *

# from http.client import HTTPConnection
import http.client

class HttpClient:
  @macronMethod
  def create_server(self, params):
    # self.connection = http.client.HTTPConnection(
    #   ''.join(params["ip"]),
    #   params["port"]
    # )

    # return self.connection
    self.console.log(self.connection)
  
  @macronMethod
  def request(self, params):
    self.connection.request(
      ''.join(params["method"]),
      ''.join(params["path"]),
      ''.join(params["body"])
    )

    return self.connection.getresponse()
  
  @macronMethod
  def close(self):
    self.connection.close()