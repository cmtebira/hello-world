##entrada de dados
x = 0
z = 0

##seleção e calculos
while x <= 4:
    n = int(input())
    if n % 2 == 0:
        z = z +1
    x = x + 1

else: # saida
    print("%d valores pares" % z)
