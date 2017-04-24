##entrada
x = 10
vetor = [0,0,0,0,0,0,0,0,0,0]
contador = 0

##processamento
while contador < x :
    vetor[contador] = int(input())
#    vetor.append(int(x[contador]))
    if vetor[contador] < 1:
        vetor[contador] = 1

##saída
    print("X[%d] = %d" % (contador, vetor[contador]))
    contador += 1

