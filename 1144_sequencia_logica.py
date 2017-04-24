##entrada
N = int(input())
i = 1

##processamento
while i <= N:
    x = i
    quadrado = x**2
    cubo = x**3
    print(x, quadrado, cubo)
    quadrado +=1
    cubo +=1
    print(x, quadrado, cubo)
    i += 1
    
