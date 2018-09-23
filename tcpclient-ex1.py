import socket

target_host = "127.0.0.1"
target_port = "9999"

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,int(target_port)))

#send some data
#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send("AAABBBCCC")

#receive some data
response = client.recv(4096)

print response
