## entrada de dados
numero = int(input())
divisor = 0
i = 1 # contador

## calculos
while 0 < i <= numero:
    divisor = numero%i
    if divisor == 0:
        print(i) # saida
    i += 1 

## saida
