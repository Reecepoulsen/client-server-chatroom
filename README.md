# Overview
This project is a client/server chatroom. You can start the server by running 'python server.py' and it will start listening for connections from clients. After the server has been started, clients can connect by running 'python client.py'. You can connect as many clients as you would like. The server starts a thread to manage each client so it can maintain many connections at the same time. When a client is started, they are prompted for a nickname for the server to know them by and then they can send messages as they please. WHen a new client joins a message is broadcasted to all of the other clients to let them know. 

There are two types of messages that a client can send: a broadcast or a message to a specific person. Broadcast messages are the default. If you @ someone in the message, then it will only send the message to that specific person. Group messages can be made by @ing multiple people.

I wrote this software to help me understand how to use the python socket library and gain further insight into the client/server relationship. 

## Demonstration Video
[Chatroom Using Python's Socket Library](https://youtu.be/ZmCCptoTvcs)

# Network Communication

* Client/Server
* HOST = 127.0.0.1 (Localhost) 
* PORT = 42000
* Socket Stream
* Messages are encoded to and from ASCII


# Development Environment
* VSCode
* Python
* Socket library
* Threading library

# Useful Websites
* [Socket Library Documentation](https://docs.python.org/3.6/library/socket.html)
* [Threading Library Documentation](https://docs.python.org/3/library/threading.html)

# Future Work

* Add functionality for a user to type goodbye and then be disconnected from the chat
* Build an app that interfaces with the server
* Add the ability for the server fetch something like a web request or data from a database