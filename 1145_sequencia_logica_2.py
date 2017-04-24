##entrada
valores = input().split()
x = int(valores[0])
y = int(valores[1])
numero = 1
i = 1

##processamento
while numero < y:
    while i < x and numero < y:
        print(numero, end=" ")
        i += 1
        numero += 1
    if i == x and numero < y:
        print(numero)
        numero += 1
    i = 1
print(numero)
