d1 = input().split(" ")
h1 , m1, s1 = input().split(":")
d2 = input().split(" ")
h2, m2, s2 = input().split(":")
dia = int(d2[1]) - int(d1[1])
hora = int(h2) - int(h1)
if hora < 0:
    hora = hora + 24
    dia = dia -1
minuto = int(m2) - int(m1)
if minuto <0:
    minuto = minuto + 60
    hora = hora - 1
segundo = int(s2) - int(s1)
if segundo < 0:
    segundo = segundo + 60
    minuto = minuto - 1
if dia < 0:
    dia < 0
print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minuto)
print("%d segundo(s)" % segundo)
