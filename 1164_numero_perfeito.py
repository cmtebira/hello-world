##entrada
quant_testes = int(input())
soma = 0 #acumulador
i = 1 # contador
z = 1 # contador

##processamento
while z <= quant_testes:
    x = int(input())
    while i < x:
        if x%i == 0:
            soma += i
        i += 1
    if soma == x:
        print("%d eh perfeito" % x) # saida
    if soma != x:
        print("%d nao eh perfeito" % x) # saida
    soma = 0
    i = 1
    z += 1
