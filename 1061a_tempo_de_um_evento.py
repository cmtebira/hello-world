##entrada
d1 = int(input("Dia "))
e1 = input().split(" : ")
h1 = int(e1[0])
m1 = int(e1[1])
s1 = int(e1[2])

d2 = int(input("Dia "))
e2 = input().split(" : ")
h2 = int(e2[0])
m2 = int(e2[1])
s2 = int(e2[2])

##selecao e calculos
dia = d2 - d1

hr = h2 - h1
if(hr < 0):
	hr = 24 + hr
	dia = dia - 1

mn = m2 - m1 
if(mn < 0):
	mn = 60 + mn
	hr = hr - 1
	
seg = s2 - s1
if(seg < 0):
	seg = 60 + seg
	mn = mn - 1

if(dia <= 0):
	dia = 0

##saida
print ("%d dia(s)" %dia)
print ("%d hora(s)" %hr)
print ("%d minuto(s)" % mn)
print ("%d segundo(s)" %seg)
