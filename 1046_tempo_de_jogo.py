##entrada de dados
hora_inicio, hora_fim = input().split()
hora_inicio = int(hora_inicio)
hora_fim = int(hora_fim)

##seleção e calculos
if hora_inicio > hora_fim:
    duracao = (24 - hora_inicio) + hora_fim
    print ("O JOGO DUROU %d HORA(S)" % duracao)

elif hora_inicio < hora_fim:
    duracao = (hora_fim - hora_inicio)
    print ("O JOGO DUROU %d HORA(S)" % duracao)

else:
    print ("O JOGO DUROU 24 HORA(S)")
