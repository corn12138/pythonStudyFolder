# server.py
from socket import *
from threading import Thread

clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                broadcast(msg, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, client_socket):
    # for client in clients:
    #     if client != client_socket:
    #         try:
    #             client.send(message.encode('utf-8'))
    #         except:
    #             remove(client)
    msg = input(">")
    client_socket.send(msg.encode("utf-8"))

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

if __name__ == "__main__":
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8900))
    server_socket.listen(5)
    print("Server started and listening on port 8900")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")
        thread = Thread(target=handle_client, args=(client_socket,))
        thread.start()
        thread.join()

        client_socket.close()
        server_socket.close()

