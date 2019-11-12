# Chat server
import socket

messages = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2000))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connection from', addr)
            
            while True:
                data = conn.recv(1024).decode('utf8')
                if data:
                    if data.startswith('send'):
                        messages.append(f'{addr[0]}: {data[4:]}')
                    elif data.startswith('get'):
                        conn.sendall('\n'.join(messages[-10:]).encode('utf8'))
                    break
                    