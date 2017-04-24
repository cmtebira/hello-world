##entrada
diainicio = int(input("Dia "))
horainicio = input().split(":")
hinicio = int(horainicio[0])
minicio = int(horainicio[1])
sinicio = int(horainicio[2])

diafinal = int(input("Dia "))
horafinal = input().split(":")
hfinal = int(horafinal[0])
mfinal = int(horafinal[1])
sfinal = int(horafinal[2])

##selecao e calculos
dia = diafinal - diainicio

hora = hfinal - hinicio
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = mfinal - minicio 
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1
	
segundos = sfinal - sinicio
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

##saida
print ("%d dia(s)" %dia)
print ("%d hora(s)" %hora)
print ("%d minuto(s)" %minuto)
print ("%d segundo(s)" %segundos)
