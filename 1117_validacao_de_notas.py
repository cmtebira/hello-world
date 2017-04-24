## entrada de dados
x = 0
media = 0

## calculos
while x < 2:
    nota = float(input())    
    if nota >= 0 and  nota <=10:
        media += nota
        x += 1
    else:
        print("nota invalida")

## saida
print("media = %.2f" % (media / 2))
