## entrada de dados
soma = 1 # valor de "S"
numerador = 3
denominador = 2

## calculos
while 3 <= numerador <= 39:
    soma += numerador / denominador
    numerador += 2
    denominador *= 2
    
## saida
print("%.2f" % soma)
