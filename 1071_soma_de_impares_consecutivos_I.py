##entrada
x = int(input())
y = int(input())
soma = 0
temp = 0
impar = 0

##calculos e selecao
if x >= y:
    temp = x
    x = y
    y = temp
    i = x
while i >= x and i < y:
    if i > x:
        if i % 2 != 0:
            impar = i
            soma = soma + impar
    i = i + 1
else:
    print("%d" % soma)
