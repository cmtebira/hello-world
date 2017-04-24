di = input()
hi , mi, si = input().split(":")
df = input()
hf, mf, sf = input().split(":")
dia = int(df) - int(di)
hora = int(hf) - int(hi)
if hora < 0:
    hora = hora + 24
    dia = dia -1
minuto = int(mf) - int(mi)
if minuto <0:
    minuto = minuto + 60
    hora = hora - 1
segundo = int(sf) - int(si)
if segundo < 0:
    segundo = segundo + 60
    minuto = minuto - 1
if dia < 0:
    dia < 0
print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minuto)
print("%d segundo(s)" % segundo)
