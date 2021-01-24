import sys


#A python program to illustrate Scytale Cipher Technique 
def scytale(text):
	l = len(text)
	#print(str(l))
	for i in range(1,l//2+1): 
		#print("La i vale : " + str(i))
		for j in range(l//i):
			#print("La j vale : " + str(j))
			palabras = []
			for k in range(0,l-j,l//i):
				#print("La j+k vale : " + str(j+k))
				palabras.append(text[j+k])
			print(''.join(palabras))


#encrypt/decrypt our text
with open(sys.argv[1], "r") as f:
	text = f.read()
	scytale(text)

