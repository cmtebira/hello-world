##entrada
quant_testes = int(input())
z = 1



##processamento
while z <= quant_testes:
    valor_inteiro = int(input())
    if valor_inteiro % 2 == 0:
        if valor_inteiro == 2:
            print("%d eh primo" % valor_inteiro)
        else:
            print("%d nao eh primo" % valor_inteiro)
    else:
        div = 3
        primo = True
        while div <= valor_inteiro**0.5 and primo == True:
            if valor_inteiro % div == 0:
##                print("Não é primo pois dividiu por %d" % div)
                primo = False
                print("%d nao eh primo" % valor_inteiro)
            div += 2
        if primo == True:
            print("%d eh primo" % valor_inteiro)
    z += 1

##saida
