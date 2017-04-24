## entrada de dados
coord_x, coord_y = input().split()
coord_x = float(coord_x)
coord_y = float(coord_y)

## calculos da selecao
if coord_x == 0.0 and coord_y == 0.0:
    print("Origem")
elif coord_x == 0.0:
    print("Eixo Y")
elif coord_y == 0.0:
    print("Eixo X")
elif coord_x > 0.0 and coord_y > 0.0:
    print("Q1")
elif coord_x < 0.0 and coord_y > 0.0:
    print("Q2")
elif coord_x < 0.0 and coord_y < 0.0:
    print("Q3")
else coord_x > 0.0 and coord_y < 0.0:
    print("Q4")

## saida

