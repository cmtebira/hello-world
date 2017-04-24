##entrada

i = 1

##processamento
while True:
    x = int(input()) ## variavel inteira
    if x == 0:
        break
    while i < x:
        print(i, end=" ")
        i += 1
    else:
        if i == x:
            print(x)
        i = 1    
