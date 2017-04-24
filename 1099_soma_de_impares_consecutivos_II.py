##entrada
quant_testes = int(input())
z = 1
soma = 0
temp = 0
impar = 0

##calculos e selecao
while z <= quant_testes:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if x >= y:
        temp = x
        x = y
        y = temp
        i = x
    elif x < y:
        i = x
    while i >= x and i < y:
        if i > x:
            if i % 2 != 0:
                impar = i
                soma = soma + impar
        i = i + 1
    print(soma)
    soma = 0
    impar = 0
    z += 1
