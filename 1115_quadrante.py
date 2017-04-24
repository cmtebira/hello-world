## entrada de dados


## calculos da selecao
while True:
    coord_x, coord_y = input().split()
    coord_x = int(coord_x)
    coord_y = int(coord_y)
    if coord_x == 0 or coord_y == 0:
        break
    elif coord_x > 0 and coord_y > 0:
        print("primeiro")
    elif coord_x < 0 and coord_y > 0:
        print("segundo")
    elif coord_x < 0 and coord_y < 0:
        print("terceiro")
    elif coord_x > 0 and coord_y < 0:
        print("quarto")

## saida
