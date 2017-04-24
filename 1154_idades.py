## entrada de dados
soma = 0
media = 0
x = 1

## calculos
while x >= 0:
    numero = int(input())
    if numero < 0:
        break
    soma += numero
    media = soma / x 
    
    x = x + 1

## saida
print("%.2f" % media)
