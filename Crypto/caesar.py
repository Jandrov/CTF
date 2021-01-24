import sys

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length=len(alphabet)
'''
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
			print(palabras)

			'''
#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i] 
		'''
		n = ord(char)
		if (n < 65 or n > 97+25 or n in range(65+26, 97)):
			result += char

		# Encrypt uppercase characters 
		elif (char.isupper()): 
			result += chr((n + s-65) % 26 + 65) 

		# Encrypt lowercase characters 
		else: 
			result += chr((n + s - 97) % 26 + 97) 
		'''
		if char == " ": 
			result += char
		else:
			#print(char)
			pos = alphabet.index(char)
			result += alphabet[(pos + s) % length]

	return result 

#decrypt our text
with open(sys.argv[1], "r") as f:
	res = []
	text = "BHMMZLNM SNMHFGS RPTZQD HMCDW"
	for s in range(length):
		r = encrypt(text, length-s)
		res.append(r)
		print(r,s)

	'''i = 1
	for texto in res:
		
		print("Cadena no :", i)
		scytale(texto)
		i+=1'''

