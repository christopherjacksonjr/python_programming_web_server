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
    outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
    connectionData = b"Connection: Keep-Alive\r\n"
    serverData = b"Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.33 mod_perl/2.0.11 Perl/v5.16.3\r\n\r\n"
    headers = outputdata + connectionData + serverData

    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      f = open(filename[1:], "r")
      fileContent = f.read()
      response = 'HTTP/1.1 200 OK\r\n' + headers.decode() + fileContent
      connectionSocket.sendall(response.encode())
      connectionSocket.close()

    except Exception as e:
      print("Exception: ", e)
      response = 'HTTP/1.1 404 Not Found\r\n' + headers.decode() + '<h1>404 Not Found</h1>'
      connectionSocket.sendall(response.encode())
      connectionSocket.close()

  serverSocket.close()
  sys.exit()

if __name__ == "__main__":
  webServer(13331)
