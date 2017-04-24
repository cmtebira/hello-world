##entrada

alcool = 0 ## código 1
gasolina = 0  ## código 2
diesel = 0  ## código 3
fim = 0  ## código 4

##calculos e selecao
while True:
    tipo_combustivel = int(input())
    if tipo_combustivel == 4:
        break
    elif tipo_combustivel == 1:
        alcool += 1
    elif tipo_combustivel == 2:
        gasolina += 1
    elif tipo_combustivel == 3:
        diesel += 1

## saida
print("MUITO OBRIGADO")
print("Alcool: %d" % alcool)
print("Gasolina: %d" % gasolina)
print("Diesel: %d" % diesel)
