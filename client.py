import socket 
import threading

#------------------------------------------------------------------------------
# Set up globals
#------------------------------------------------------------------------------
nickname = input("Choose a nickname: ") # Get nickname to set up with server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("127.0.0.1", 42000))    # Connect client to server at the given address

#------------------------------------------------------------------------------
# Receives a message from server and displays it.
# if an exception is raised, we will close the connection
#------------------------------------------------------------------------------
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            # if we get keyword NICK then the server wants a nickname to store
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break

#------------------------------------------------------------------------------
# Gets input from user for messages to send. Format's message, 
# then sends it to the server
#------------------------------------------------------------------------------
def write():
    while True:
        text = input("")
        message = f'({nickname}) :: {text}'
        client.send(message.encode('ascii'))

#------------------------------------------------------------------------------
# Set up a receiving thread and a writing thread so the client can write and
# receive in parallel
#------------------------------------------------------------------------------
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()