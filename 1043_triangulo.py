##entrada de dados
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)

##selecao e saida
if((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
    perimetro=(a+b+c)
    print("Perimetro = %.1f" %perimetro)
else:
    area =(a+b)*c/2
    print("Area = %.1f" %area)
