##entrada
quant_testes = int(input())
i = 1 # contador laço interno
z = 1 # contador laço externo

##processamento
while z <= quant_testes:
    teste = input().split()
    pa = int(teste[0])
    pb = int(teste[1])
    g1 = float(teste[2])
    g2 = float(teste[3])
    seculo = True

    while pa <= pb and seculo:
        if i > 100:
            print("Mais de 1 seculo.")
            seculo = False

        else:
            pa = int(pa + ((pa * g1) / 100))
            pb = int(pb + ((pb * g2) / 100))   
            if pa > pb:
                print("%d anos." % i)
            i += 1
    i = 1
    z +=1

##saida


