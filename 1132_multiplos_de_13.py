##entrada
x = int(input())
y = int(input())
soma = 0
i = 0

##calculos e selecao
if x >= y:
    temp = x
    x = y
    y = temp
i = x
while i >= x and i <= y:
    if i%13 == 0:
        i += 1
    else:
        soma += i
        i = i + 1

## saida
print(soma)
