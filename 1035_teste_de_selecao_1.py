entrada = input()
separa_ent = entrada.split()
A = int(separa_ent[0])
B = int(separa_ent[1])
C = int(separa_ent[2])
D = int(separa_ent[3])
if (B > C and D > A) and ((C + D) > (A + B)) and ( C > 0 and D > 0) and (A % 2 == 0):
    print ("Valores aceitos")
else:
    print("Valores nao aceitos")
