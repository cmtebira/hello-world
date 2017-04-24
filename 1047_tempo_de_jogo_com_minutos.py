##entrada de dados
hora_inicio, min_inicio, hora_fim, min_fim = input().split()
hora_inicio = int(hora_inicio)
min_inicio = int(min_inicio)
hora_fim = int(hora_fim)
min_fim = int(min_fim)

##seleção e calculos
if hora_inicio == hora_fim and min_inicio == min_fim:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else :
    if hora_inicio > hora_fim:
        duracao_hr = (24 - hora_inicio) + hora_fim
    elif hora_inicio < hora_fim:
        duracao_hr = (hora_fim - hora_inicio)
    if min_inicio > min_fim:
        duracao_min = (60 - min_inicio) + min_fim
        duracao_hr -= 1
    elif min_inicio < min_fim:
        duracao_min = (min_fim - min_inicio)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao_hr, duracao_min))
