##entrada
lista = []
soma = 0
i = 0

##calculos e selecao
while True:
    entrada = input().split()
    M = int(entrada[0])
    N = int(entrada[1])
    i = M
    if M <= 0 or N <= 0:
        break
    if M >= N:
        temp = M
        M = N
        N = temp
        i = M
    while i >= M and i <= N:
        print(i,"", end="")
        soma += i
        i = i + 1
    
    print("Sum=%d" % soma)
    soma = 0
    lista = []
