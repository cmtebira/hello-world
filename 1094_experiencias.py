##entrada
quant_testes = int(input())
z = 1
tt_cobaias = 0
rato = 0
sapo = 0
coelho = 0

##calculos e selecao
while z <= quant_testes:
    experimento = input().split()
    quantia = int(experimento[0])
    tipo = experimento[1]
    tt_cobaias += quantia
    if tipo == "R":
        rato += quantia
    elif tipo == "S":
        sapo += quantia
    elif tipo == "C":
        coelho += quantia
    z += 1

##saida
print("Total: %d cobaias" % tt_cobaias)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f %s" % (float((coelho/tt_cobaias) * 100), "%"))
print("Percentual de ratos: %.2f %s" % (float((rato/tt_cobaias) * 100), "%"))
print("Percentual de sapos: %.2f %s" % (float((sapo/tt_cobaias) * 100), "%"))
