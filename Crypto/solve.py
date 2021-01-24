from pwn import * # pip install pwntools

result = 'a'*43*7
result = list(result)
#print(result)
num1 = 0
num2 = 1
for _ in range(294):
	r = remote('2020.redpwnc.tf', 31284)
	num1 += 1
	num2 += 1
	r.sendline(str(num1).encode())
	r.sendline(str(num2).encode())
	line = r.recvline().decode('ascii')
	binstring = line.split('Ciphertext: ')[-1][:-1]
	#print(binstring)
	lb = 2**num1
	ub = 2**num2 - 1
	l = list(binstring)
	for i in range(0, len(l), len(bin(lb)[2:])):
		l[i] = str(int(l[i]) ^ 1)
		result[i] = l[i]

	if not 'a' in result:
		result = "".join(result)
		print(result) 
		break
result = "".join(result)
print(result)