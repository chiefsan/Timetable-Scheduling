
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 3333))
'''
while True:
    fragment = s.recv(1024)
    #fragment = Fragment.strToFragment(str(fragment, 'utf-8'))
    #fragment = updateFragment(fragment)
    #s.send(bytes(str(fragment), 'utf-8'))
    print (fragment)
'''
port = s.recv(1024)
port = str(port, 'utf-8')
port = int(port)
print (port)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))
s.listen(5)
connect, addr = s.accept()
connect.sendto(bytes('lol', 'utf-8'), addr)
connect.close()


