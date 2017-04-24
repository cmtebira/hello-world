## entrada de dados

x = 0 # contador
gols_inter = 0
gols_gremio = 0
soma_gols_inter = 0
soma_gols_gremio = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
total_de_grenais = 0
novo_grenal_sim_nao = 3

## processamentos
while x < 1:
    gols_marcados = input().split()
    gols_inter = int(gols_marcados[0])
    gols_gremio = int(gols_marcados[1])
    soma_gols_inter += gols_inter
    soma_gols_gremio += gols_gremio
    total_de_grenais += 1
    if gols_inter == gols_gremio:
        empates += 1
    if gols_inter > gols_gremio:
        vitorias_inter += 1
    if gols_gremio > gols_inter:
        vitorias_gremio += 1
        
    novo_grenal_sim_nao = int(input("Novo grenal (1-sim 2-nao)\n"))
    if novo_grenal_sim_nao == 1:
        x = 0
    elif novo_grenal_sim_nao == 2:
        x += 1
    else:
        novo_grenal_sim_nao = int(input("Novo grenal (1-sim 2-nao)\n"))

## saida
print("%d grenais" % total_de_grenais)
print("Inter:%d" % vitorias_inter)
print("Gremio:%d" % vitorias_gremio)
print("Empates:%d" % empates)
if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
if vitorias_gremio > vitorias_inter:
    print("Gremio venceu mais")
