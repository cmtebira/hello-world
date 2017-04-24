## entrada de dados
A, B, C = input().split()
lado_maior = A
lado_medio = B
lado_menor = C
lado_maior = float(lado_maior)
lado_medio = float(lado_medio)
lado_menor = float(lado_menor)
temp = 0

## calculos da selecao
## ordem decrescente
if lado_maior < lado_medio:
    temp = lado_maior
    lado_maior = lado_medio
    lado_medio = temp
    temp = 0
if lado_maior < lado_menor:
    temp = lado_maior
    lado_maior = lado_menor
    lado_menor = temp
    temp = 0
if lado_medio < lado_menor:
    temp = lado_medio
    lado_medio = lado_menor
    lado_menor = temp
    temp = 0

##tipos de triangulos
A = lado_maior
B = lado_medio
C = lado_menor

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2) == (B**2) + (C**2):
        print("TRIANGULO RETANGULO")
    if (A**2) > (B**2) + (C**2):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < (B**2) + (C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B and A == C and B == C:
        print("TRIANGULO EQUILATERO")
    else:
        if A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

## saida
