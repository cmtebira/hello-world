##entrada
n = int(input())
fatorial = 1
i = 0 # contador

##processamento
while i >= 0 and i < n:
    fatorial = fatorial * (n - i)
    i += 1

##saida
print(fatorial)
