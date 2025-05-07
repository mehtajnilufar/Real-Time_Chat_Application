import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print("\n" + msg)
        except:
            print("An error occurred.")
            sock.close()
            break

def send_messages(sock):
    while True:
        msg = input()
        sock.send(msg.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

name = input("Enter your name: ")
client.send(f"{name} has joined the chat!".encode())

thread_recv = threading.Thread(target=receive_messages, args=(client,))
thread_recv.start()

thread_send = threading.Thread(target=send_messages, args=(client,))
thread_send.start()
