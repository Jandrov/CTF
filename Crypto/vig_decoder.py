from string import ascii_lowercase
# Function to print the output  
def printTheArray(arr, n):  
  
    for i in range(0, n):  
        #print(translateMessage(arr[i],ciphertext)[0])
        print(arr[i], end= "")
    print()  
      
  
# Function to generate all binary strings  
def generateAllBinaryStrings(n, arr, i, set1, set2):  
  
    if i == n: 
        printTheArray(arr, n)  
        return
      
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = set1[i]
    generateAllBinaryStrings(n, arr, i + 1, set1, set2)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = set2[i]
    generateAllBinaryStrings(n, arr, i + 1, set1, set2)  
  



    #text = translateMessage(set2, ciphertext)

    #print(text)





def translateMessage(key, message, mode=""):
    translated = [] # stores the encrypted/decrypted message string
    translated2 = []
    key = ''.join(key[i % len(key)] for i in range(len(message))).lower()
    #print(key)
    keyIndex = 0

    for symbol in message: # loop through each character in message
        num = ascii_lowercase.find(symbol)
        num2 = num+26
        if num != -1: # -1 means symbol.lower() was not found in ascii_lowercase
            if mode == 'keymode':
                num = num//2
                num2 = num2//2
                translated.append(ascii_lowercase[num])
                translated2.append(ascii_lowercase[num2])
            else:
                #print("Descifrando " + message)
                num -= ascii_lowercase.find(key[keyIndex]) # subtract if decrypting

                num %= len(ascii_lowercase) # handle the potential wrap-around

                # add the encrypted/decrypted symbol to the end of translated.
                translated.append(ascii_lowercase[num])

                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
        else:
            # The symbol was not in ascii_lowercase, so add it to translated as is.
            translated.append(symbol)
            keyIndex+=1

    return ''.join(translated),"".join(translated2)


pseudokey= "iigesssaemk"
ciphertext = """z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"""
'''set1,set2 = translateMessage("loquesea", pseudokey, "keymode")
n = 11
arr = [None] * n  
  
generateAllBinaryStrings(n, arr, 0, set1, set2)  '''
'''with open("salida.txt","r") as f:
    line = f.readline()
    while line != "":
        print(translateMessage(line, ciphertext)[0])
        line = f.readline()'''
with open('key.txt','r') as f:
    print(translateMessage(f.read(), ciphertext)[0])
