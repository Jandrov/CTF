

with open('salida2.txt','r') as f:
	line = f.readline()
	flag = ''
	while line != '':
		line = line.split('\n')[0]
		n = int(line,2)
		flag += chr(n)
		line = f.readline()

print(flag)