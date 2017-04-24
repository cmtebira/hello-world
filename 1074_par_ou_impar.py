##entrada
n = int(input())
x = 1
i = 0

##processamento
while x <= n:
    valor = int(input())
    if valor == 0:
        print("NULL") # saida
    else:
        if valor % 2 == 0:
            print("EVEN", end = " ") # saida
        else:
            print("ODD", end = " ") # saida
        if valor > 0:
            print("POSITIVE") # saida
        else:
            print("NEGATIVE") # saida
    x = x + 1

# saida
