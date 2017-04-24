##entrada
x = 100
vetor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contador = 0

##processamento
while contador < x :
    vetor[contador] = float(input())
#    vetor.append(int(x[contador]))
    if vetor[contador] <= 10:
##        vetor[contador] = 1

##saída
        print("A[%d] = %.1f" % (contador, vetor[contador]))
    contador += 1

