##entrada de dados
x = 0
z = 0
s = 0
##seleção e calculos
while x <= 5:
    n = float(input())
    if n > 0.0:
        s = s + n
        z = z +1
    x = x + 1

else: # saida
    m = s / z
    print("%d valores positivos" % z)
    print("%.1f" % m)
