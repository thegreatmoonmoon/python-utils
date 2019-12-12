import socket

def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
       s.connect((ip, int(port)))
       s.shutdown(2)
       return True
    except:
       return False

for i in range (80, 1000):
   if isOpen('x.x.x.x', i) == True:
      print("port {}: Open".format(i))