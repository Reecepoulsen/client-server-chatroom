import threading
import socket

#------------------------------------------------------------------------------
# Set up globals
#------------------------------------------------------------------------------
clients = []
nicknames = []

# create a server obj, bind it to the host and port, then start listening 
# for connection requests
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 42000
server.bind((HOST, PORT))
server.listen()

#------------------------------------------------------------------------------
# Gets the nickname for a particular client
#------------------------------------------------------------------------------
def getNickname(client):
    index = clients.index(client)
    return nicknames[index]

#------------------------------------------------------------------------------
# Broadcasts a message to all clients besides the sender
#------------------------------------------------------------------------------
def broadcast(sender, message):
    senderNickname = getNickname(sender)
    for client in clients:
        curNickname = getNickname(client)
        # Send message to everyone but the sender
        if senderNickname != curNickname:
            client.send(message.encode('ascii'))

#------------------------------------------------------------------------------
# If the message contains another client's nickname, it will only send to
# that client specifically. 
#------------------------------------------------------------------------------
def send(sender, message):
    sent = False
    senderNickname = getNickname(sender)
    for name in nicknames:
        if "@" + name.lower() in message.lower():
            recipientNickname = name
            index = nicknames.index(recipientNickname)
            recipient = clients[index]
            recipient.send(message.encode('ascii'))
            # We already sent the message, toggle sent to True so we don't broadcast
            sent = True
    return sent

#------------------------------------------------------------------------------
# Removes client from client list, disconnects socket, and removes nickname
# from nickname list to maintain data integrity
#------------------------------------------------------------------------------
def disconnect(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(client, f'{nickname} left the chat')
    nicknames.remove(nickname)

#------------------------------------------------------------------------------
# Handle's when a client sends a message. Checks to see if the message
# has specific recipient(s) with send function. If the send function 
# returns false, that means that we should broadcast the message instead.
# If an exception is raised, we should disconnect the client. 
#------------------------------------------------------------------------------
def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if not send(client, message):
                broadcast(client, message)
        except:
            disconnect(client)
            break

#------------------------------------------------------------------------------
# Connects a client to the server, requests a nickname, then stores nickname
# and the client in their respective lists. Broadcasts a message for each
# client connected to other clients. 
# Sets up an individual handle thread for each client.
#------------------------------------------------------------------------------
def receive():
    print(f'Server is listening on Port {PORT}')
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}')
        broadcast(client, f'{nickname} joined the chat')
        client.send('Connected to the Server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

receive()   # Starts program

# Ways that I can make this better
# 1. Add a GUI
# 2. Add a disconnect function(type goodbye)
# 3. Make the clientList a map and store each client's information