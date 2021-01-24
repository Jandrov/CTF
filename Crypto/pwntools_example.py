from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
	line = r.recvline()
	return json.loads(line.decode())

def json_send(hsh):
	request = json.dumps(hsh).encode()
	r.sendline(request)


def decode(encoding, encoded):
	if encoding == "base64":
		decoded = base64.b64decode(encoded.encode('ascii')).decode('ascii') 
	elif encoding == "hex":
		decoded = bytes.fromhex(encoded).decode('ascii')
	elif encoding == "rot13":
		decoded = codecs.encode(encoded, 'rot_13')
	elif encoding == "bigint":
		decoded = bytes.fromhex(encoded[2:]).decode('ascii')
	elif encoding == "utf-8":
		decoded = "".join([chr(b) for b in encoded])

	return {"decoded": decoded}



'''
print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])'''

while True:
	received = json_recv()
	encoding = received["type"]
	encoded = received["encoded"]
	if encoding == "flag":
		print(encoded)
		break

	to_send = decode(encoding, encoded)
	json_send(to_send)


