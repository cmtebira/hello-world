##entrada

maior = 0
lista = []
i = 1
achou = False

##processamento
while i <= 100:
    x = int(input())
    lista.append(x)
    if x > maior:
        maior = x
    i += 1
i = 0
p = maior
while i < len(lista):
	if lista[i] == p:
		achou = True
		i += 1
		break
	i+=1
if achou:
	print(p)
	print(i)


