import socket
import threading

clients = []

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(f"[{addr}] {msg}")
            broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen()

print("[STARTED] Server started on port 9999. Waiting for connections...")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
