import sys
import socket

url = input("Enter website url for whois query: ")

try:
    domain = url.split('/')[2]
except IndexError as e:
    print('invalid URL')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('whois.iana.org', 43))
s.send((domain + "\r\n").encode())

response = b''
while True:
    data = s.recv(4096)
    response += data
    if not data:
        break

decoded_response = response.decode()

whois_server_list = []

for line in decoded_response.split('\n'):
    if ':' in line:
        keyword, value = map(str.strip, line.split(':', 1))
        if keyword.lower() == 'whois':
            whois_server_list.append(value)

if whois_server_list:
    for whois_server in whois_server_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((whois_server, 43))
        s.send((domain + "\r\n").encode())

        response = b''
        while True:
            data = s.recv(4096)
            response += data
            if not data:
                break

        print(response.decode())

else:
    print(f"WHOIS server not found {domain}")
    
