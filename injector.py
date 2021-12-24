#!/bin/env python3

import urllib.request
import sys
import time

target = sys.argv[1]
port = sys.argv[2]
header = sys.argv[3]
payload_list = sys.argv[4]

try:
    client.connect((target, int(port)))
except ConnectionError:
    print('[-] Cannot conenct to target!')

def send_payloads():
    print('[*] Connecting to target...')
    print('[*] Sending payloads...')

    stream_reader = open(payload_list, 'r')
    for payload in stream_reader:
        server = urllib.request.urlopen(f'{target}:{port}/index.php?{header}=Buffer{payload}')

        print('[*] PAYLOAD: ' + payload, end='')

        time.sleep(0.02)

if __name__ == '__main__':
    send_payloads()
    print('\n')
