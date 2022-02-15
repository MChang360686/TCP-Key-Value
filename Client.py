#!/usr/bin/env python3
import socket

# Client
HOST = '127.0.0.1'
HOST = input("Enter IP Address (Default 127.0.0.1)")
Socket = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, Socket))
print("Please enter a command (Case Sensitive)")

while True:
    response = client.recv(1024)
    response = response.decode("utf-8")
    print(response)
    command = input(">")
    command = command.encode("utf-8")
    client.send(command)