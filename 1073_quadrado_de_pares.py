##entrada
n = int(input())
x = 1
quadrado = 0

##processamento
while x <= n:
    if x % 2 ==0:
        quadrado = x**2        
        print("%d^2 = %d" % (x, quadrado)) # saida
    x = x + 1

# saida
