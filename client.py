# Chat client
import socket
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 2000))
    
        s.sendall('get'.encode('utf8'))
        print(s.recv(4096).decode('utf8'))

    new_msg = input('Send Message: ')
    if new_msg == 'exit': exit(0)

    if new_msg:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 2000))
            s.sendall(f'send{new_msg}\n'.encode('utf8'))