## entrada de dados
n = int(input())
x = 1

## calculos
while x <= n:
    entrada = input()
    separa_ent = entrada.split()
    N1 = float(separa_ent[0])
    N2 = float(separa_ent[1])
    N3 = float(separa_ent[2])
    N1 = N1*2
    N2 = N2*3
    N3 = N3*5
    MEDIA = (N1+N2+N3)/10
    print("%.1f" % MEDIA) # saida
    x = x + 1

## saida
