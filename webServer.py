# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  print('Ready to serve...')

  while True:
    connectionSocket, addr = serverSocket.accept()

    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      f = open(filename[1:], "r")
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      fileContent = f.read()
      response = 'HTTP/1.1 200 OK\n\n' + fileContent
      connectionSocket.sendall(response.encode())
      connectionSocket.close()

    except Exception as e:
      print("Exception: ", e)
      response = 'HTTP/1.1 404 Not Found\n\n<h1>Not Found</h1>'
      connectionSocket.sendall(response.encode())
      connectionSocket.close()

  serverSocket.close()
  sys.exit()

if __name__ == "__main__":
  webServer(13331)
