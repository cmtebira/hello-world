##entrada de dados
a,b = input().split()
a=float(a)
b=float(b)

##selecao e saida
if ((a % b == 0) or (b % a == 0)):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
