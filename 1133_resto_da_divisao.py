##entrada
x = int(input())
y = int(input())
i = 0

##calculos e selecao
if x >= y: ## coloca em ordem crescente
    temp = x
    x = y
    y = temp
i = x + 1
while i > x and i < y:
    if i%5 == 2:
        print(i) ## saida
        i += 1
    elif i%5 == 3:
        print(i) ## saida
        i += 1
    else:
        i = i + 1

## saida
