##entrada
soma = 0 #acumulador
i = 1 # contador

##processamento
while True:
    x = int(input())
    if x == 0:
        break
    while i <= 5:
        if x%2 == 0:
            soma += x
            i += 1
        x += 1
    print(soma) # saida
    soma = 0
    i = 1
    
