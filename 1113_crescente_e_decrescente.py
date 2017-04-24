##entrada


##processamento
while True:
    dupla = input().split()
    x = int(dupla[0])
    y = int(dupla[1])
    if x == y:
        break
    elif x < y:
        print("Crescente") # saida
    else:
        print("Decrescente") # saida
