# client.py
from socket import *
from threading import Thread

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(msg)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        msg = input()
        client_socket.send(msg.encode('utf-8'))
        if msg == "exit":
            client_socket.close()
            break

if __name__ == "__main__":
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8900))

    receive_thread = Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    receive_thread.join()

    send_thread = Thread(target=send_messages, args=(client_socket,))
    send_thread.start()
    send_thread.join()

    client_socket.close()