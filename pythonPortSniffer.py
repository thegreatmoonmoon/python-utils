import socket
from threading import Thread


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      print("Port {}: open".format(port))
      return True
   except:
      print("Port {}: closed".format(port))
      return False


if __name__ == "__main__":
    
   for i in range (80, 100):
      Thread(target=isOpen, args=('8.8.8.8', i, )).start()