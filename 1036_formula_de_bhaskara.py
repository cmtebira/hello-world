## entrada de dados
entrada = input()
separa_ent = entrada.split()
a = float(separa_ent[0])
b = float(separa_ent[1])
c = float(separa_ent[2])

## calculos das partes da Formula de Bhaskara
radicando = (b**2) - (4*a*c)
raiz = radicando**0.5
numerador1 = (-b + raiz)
numerador2 = (-b - raiz)
denominador = 2 * a

## saida
if radicando < 0 or denominador == 0:
    print ("Impossivel calcular")
else:
    x1 = numerador1 / denominador
    x2 = numerador2 / denominador
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
