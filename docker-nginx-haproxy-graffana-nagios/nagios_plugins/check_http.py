#!/usr/bin/env python3

import sys
import requests

def check_http(host, port):
    url = f'http://{host}:{port}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"HTTP OK - {host}:{port} responded with status {response.status_code}")
            return 0
        else:
            print(f"HTTP CRITICAL - {host}:{port} responded with status {response.status_code}")
            return 2
    except requests.RequestException as e:
        print(f"HTTP CRITICAL - {host}:{port} - {e}")
        return 2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: check_http.py <host> <port>")
        sys.exit(3)

    host = sys.argv[1]
    port = sys.argv[2]

    exit_code = check_http(host, port)
    sys.exit(exit_code)

