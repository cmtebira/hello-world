valor_lido = int(input())
notas = 0
ced_atual = 100
resto = valor_lido
while True:
    if ced_atual <= resto:
        resto -= ced_atual
        notas += 1
    else:
        print("%d notas(s) de R$%.2f" % (notas, ced_atual))
        if ced_atual == 100:
            ced_atual = 50
        elif ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 5
        elif ced_atual == 5:
            ced_atual = 2
        elif ced_atual == 2:
            ced_atual = 1
        elif ced_atual == 1:
            ced_atual = 0
            if resto == 0:
                break
        notas = 0
