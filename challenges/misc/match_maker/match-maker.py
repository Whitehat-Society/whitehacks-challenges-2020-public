#!/usr/bin/env python3

import os
import socket
from threading import Thread

FLAG = os.environ.get('FLAG', 'WHITEHACKS{placeholder}').encode()
PREPEND_COUNT = 10
BUF = list(b'0' * PREPEND_COUNT + FLAG)

IP_ADDR = '0.0.0.0'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDR, PORT))
s.listen(1)
print('Listening on port', PORT)

def sock_recv(conn, BUFFER_SIZE=1024):
    result = b""
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        result += data
        if result.endswith(b'\n'):
            break
    return result

def process_one(conn, addr):
    conn.send(b"Bet you won't be able to guess the flag, there are no print() statements muahahaha...\r\n")
    conn.send(b"Enter your input here (up to 10 chars):\r\n\r\n")

    buf = BUF.copy()
    data = sock_recv(conn)
    for i in range(min(len(BUF), len(data))):
        if chr(data[i]) not in ('\r', '\n'):
            buf[i] = data[i]

    attempt = ''.join([chr(ch) for ch in buf][:len(BUF)])
    print('Attempt by', addr, '->', data, 'Result:', attempt)
    if not attempt.endswith(FLAG.decode()):
        conn.send(b"Nice try but I've caught you!!!")
    else:
        conn.send(b"I've got nothing to say. Good bye.")
    conn.close()

while True:
    try:
        conn, addr = s.accept()
        t = Thread(target=process_one, args=(conn, addr))
        t.run()
    except:
        pass