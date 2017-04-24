##entrada
entrada = int(input())
z = 1 ## contador

##calculos e selecao
while z <= entrada:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y == 0:
        print("divisao impossivel")  ## saida
    else:
        divisao = x / y
        print("%.1f" % divisao) ## saida
    z += 1

