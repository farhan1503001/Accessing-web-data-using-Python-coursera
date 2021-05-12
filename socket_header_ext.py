import socket
#Now opening socket to access web data
opener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
opener.connect(('data.pr4e.org',80))#Now connecting the socket to port server 80 of the web
command='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
opener.send(command)#Send the command for first it is necessary to send first then we will receive

#Now reading the data
while True:
    data=opener.recv(512)#Receive 512 characters from the data at a time
    if len(data)<1:
        break
    print(data.decode(),end=' ')#Decoding the data and then printing that
opener.close()