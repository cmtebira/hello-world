## entrada de dados
A, B, C = input().split()
menor = A
medio = B
maior = C
menor = int(menor)
medio = int(medio)
maior = int(maior)
temp = 0

## calculos da selecao
if menor > medio:
    temp = menor
    menor = medio
    medio = temp
    temp = 0
if menor > maior:
    temp = menor
    menor = maior
    maior = temp
    temp = 0
if medio > maior:
    temp = medio
    medio = maior
    maior = temp
    temp = 0

## saida
print(menor)
print(medio)
print(maior)
print()
print(A)
print(B)
print(C)
