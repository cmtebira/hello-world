##entrada de dados
x = 0
z = 0

##seleção e calculos
while x <= 5:
    n = float(input())
    if n > 0.0:
        z = z +1
    x = x + 1

else: # saida
    print("%d valores positivos" % z)
