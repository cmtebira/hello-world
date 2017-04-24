##entrada
quant_testes = int(input())
z = 1
soma = 0
impar = 0
i = 1

##calculos e selecao
while z <= quant_testes:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    w = x
    while w >= x and i <= y:
        if w >= x:
            if w % 2 != 0:
                impar = w
                soma +=  impar
                i += 1
        w += 1
    print(soma)
    soma = 0
    impar = 0
    i = 1
    z += 1
