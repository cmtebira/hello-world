## entrada de dados
cod_it, quant_it = input().split()
cod_it = int(cod_it)
quant_it = int(quant_it)

## calculos das partes da Formula de Bhaskara
if cod_it == 1:
    total = quant_it * 4
elif cod_it == 2:
    total = quant_it * 4.5
elif cod_it == 3:
    total = quant_it * 5
elif cod_it == 4:
    total = quant_it * 2
elif cod_it == 5:
    total = quant_it * 1.5

## saida
print ("Total: R$ %.2f" % total)
