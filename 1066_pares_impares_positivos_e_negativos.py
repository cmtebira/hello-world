##entrada de dados
x = 0
par = 0
imp = 0
pos = 0
neg = 0

##seleção e calculos
while x <= 4:
    n = int(input())
    if n % 2 == 0:
        par += 1
    if n % 2 != 0:
        imp += 1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1
    x = x + 1

else: # saida
    print("%d valor(es) par(es)" % par)
    print("%d valor(es) impar(es)" % imp)
    print("%d valor(es) positivo(s)" % pos)
    print("%d valor(es) negativo(s)" % neg)
