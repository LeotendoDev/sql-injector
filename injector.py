#!/bin/env python3

import socket
import sys
import time

target = sys.argv[1]
port = sys.argv[2]
header = sys.argv[3]
payload_list = sys.argv[4]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((target, int(port)))
except ConnectionError:
    print('[-] Cannot conenct to target!')

def send_payloads():
    print('[*] Sending payloads...')

    stream_reader = open(payload_list, 'r')
    for payload in stream_reader:
        client.send(payload.encode('utf8'))
        print('[*] PAYLOAD: ' + payload, end='')

        time.sleep(0.02)

if __name__ == '__main__':
    send_payloads()
    print('\n')