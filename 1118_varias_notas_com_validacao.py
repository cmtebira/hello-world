## entrada de dados
condicao_de_entrada = "s"

## calculos
while condicao_de_entrada == "s":
    x = 0 # contador
    soma_das_notas = 0
    media_das_notas = 0
    continua_sim_nao = 3

##    primeiro laço interno
    while x < 2:
        nota = float(input())    
        if nota >= 0 and  nota <=10:
            soma_das_notas += nota
            media_das_notas = soma_das_notas / 2
            x += 1
        else:
            print("nota invalida")

    ## saida
    print("media = %.2f" % media_das_notas)

##    segundo laço interno
    while continua_sim_nao != 1 and continua_sim_nao != 2:
        continua_sim_nao = int(input("novo calculo (1-sim 2-nao)\n"))
        if continua_sim_nao == 1:
            condicao_de_entrada = "s"
        elif continua_sim_nao == 2:
            condicao_de_entrada = "n"
        else:
            continua_sim_nao = int(input("novo calculo (1-sim 2-nao)\n"))
