#!/usr/bin/env python3
import socket

# Initialize server
HOST = '127.0.0.1'
Socket = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, Socket))
server.listen(5)

# Create List and Dict to store keys/values and
# instructions respectively
keystore = []
command_index_dict = {"get:": " retrieve key value", "put:": " set key value or create new key:value",
                "mappings:": " get all keys and values", "keyset:": " retrieve all keys",
                "values:": " retrieve all key values from store", "help:": " list all functions",
                "bye:": " close/quit program"}
# define variables
found = False
print("Server Initialized")

client, adrs=server.accept()
print(f"Connection from {adrs}")
client.send(bytes("Server is ready to receive", "utf-8"))

while True:
    command = client.recv(1024)
    command = command.decode("utf-8")
    try:
        if command == "get":
            client.send(bytes("Enter key name", "utf-8"))
            a = client.recv(1024)
            a = a.decode("utf-8")
            print(a)
            if len(keystore) == 0:
                client.send(bytes("The list is empty", "utf-8"))
            else:
                for dictionary in keystore:
                    for key, value in dictionary.items():
                        if key == a:
                            value = str(value)
                            client.send(bytes(value, "utf-8"))
                            print(value)
                            found = True
            if found == False:
                client.send(bytes("This value does not exist", "utf-8"))
            found = False
            print("get")
        elif command == "put":
            client.send(bytes("Enter key name", "utf-8"))
            x = client.recv(1024)
            client.send(bytes("Enter key value", "utf-8"))
            y = client.recv(1024)
            if len(keystore) == 0:
                keystore.append({x: y})
            else:
                for dictionary in keystore:
                    if x in dictionary:
                        dictionary[x] = y
                    else:
                        keystore.append({x: y})
            print("put")
        elif command == "mappings":
            # list all keys and values
            keystore = str(keystore)
            client.send(bytes(keystore, "utf-8"))
            print("mappings")
        elif command == "keyset":
            # retrieve all keys from key value store
            # print
            for dictionary in keystore:
                for key, value in dictionary.items():
                    key = str(key)
                    client.send(bytes(key, "utf-8"))
            print("keyset")
        elif command == "values":
            # retrieve all values from the key value store
            # iterate through each dict in the list
            for dictionary in keystore:
                # iterate through each dict and pull value
                for key, value in dictionary.items():
                    value = str(value)
                    client.send(bytes(value, "utf-8"))
                    print(value)
            print("values")
        elif command == "help":
            # print all available functions
            # instead of the keystore, access a different dict
            # iterate through the dictionary and print
            for func, description in command_index_dict.items():
                func = str(func)
                description = str(description)
                client.send(bytes(func, "utf-8"))
                client.send(bytes(description, "utf-8"))
                print(func, description)
            print("help")
        elif command == "bye":
            client.close()
            print("bye")
            break
    except KeyError:
        print("No such function exists")

# At this point the loop should stop,
# and the client should be closed.
server.close()
quit()