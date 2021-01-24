with open('a.txt','r') as g:
    line = g.readline()[:-1]
    n=7
    a = [line[i:i+n] for i in range(0, len(line), n)]
    line = g.readline()[:-1]
    b = [line[i:i+n] for i in range(0, len(line), n)] 
    with open('salida.txt','w') as f:
        for elem in a:
            f.write(elem+'\n')
    with open('salida2.txt','w') as f:
        for elem in b:
            f.write(elem+'\n')
