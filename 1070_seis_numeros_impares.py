##entrada de dados
conta_impar = 0
x = int(input())

##seleção e calculos
while conta_impar < 6:
    if x % 2 != 0:
        print(x)
        conta_impar += 1
    x = x + 1
