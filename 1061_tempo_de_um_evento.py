##entrada de dados
d1 = input().split()
d1 = int(d1[1])
e1 = input()
se1 = e1.split(":")
h1 = int(se1[0])
m1 = int(se1[1])
s1 = int(se1[2])

d2 = input().split()
d2 = int(d2[1])
e2 = input()
se2 = e2.split(":")
h2 = int(se2[0])
m2 = int(se2[1])
s2 = int(se2[2])

##seleção e calculos
dia = d2 - d1

if h1 > h2:
    hr = (24 - h1) + h2
    dia -= 1
elif h1 < h2:
    hr = (h2 - h1)
if m1 > m2:
    mn = (60 - m1) + m2
    hr -= 1
elif m1 < m2:
    mn = (m2 - m1)
if s1 == s2:
    sg = 0
elif s1 > s2:
    sg = (60 - s1) + s2
    mn -= 1
elif s1 < s2:
    sg = (s2 - s1)

##saida
print("%d dia(s)" % dia)
print("%d hora(s)" % hr)
print("%d minuto(s)" % mn)
print("%d segundo(s)" % sg)
      
      
