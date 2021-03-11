import socket
from PIL import Image

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1002)) 
print("Waiting for connection!") 
server.listen()
client_socket, client_address = server.accept()
print("Connected! Hello: " + str(client_address)) 
file = open('server_image.jpg', "wb")
    
while 1:
    image_chunk = client_socket.recv(1024)
    if image_chunk == bytes(0): break
    file.write(image_chunk)  

file.close()
print("Img saved!")
#im = Image.open("server_image.jpg")  
#im.show()


client_socket.close()
print("Connection closed, working on img.")

#