##entrada
n = int(input())
x = 1
dentro = 0
fora = 0

##processamento
while x <= n:
    valor = int(input())
    if valor >= 10 and valor <= 20:
        dentro += 1
    elif valor < 10 or valor > 20:
        fora += 1
    x = x + 1
else:   # saida
    print("%d in" % dentro)
    print("%d out" % fora)
