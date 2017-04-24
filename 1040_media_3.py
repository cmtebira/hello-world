## entrada de dados
entrada = input()
separa_ent = entrada.split()
N1 = float(separa_ent[0])
N2 = float(separa_ent[1])
N3 = float(separa_ent[2])
N4 = float(separa_ent[3])

## calculos
N1 = N1*2
N2 = N2*3
N3 = N3*4
N4 = N4*1
MEDIA = (N1+N2+N3+N4)/10
print("Media: %.1f" % MEDIA)


## saida
if MEDIA >= 7.0:
    print ("Aluno aprovado.")
elif MEDIA >= 5.0 and MEDIA <= 6.9:
    print ("Aluno em exame.")
    N5 = float(input())
    print ("Nota do exame: %.1f" % N5)
    MEDIA_FINAL = (MEDIA + N5)/2
    if MEDIA_FINAL >= 5.0:
        print ("Aluno aprovado.")
    else:
        print ("Aluno reprovado.")
    print ("Media final: %.1f" % MEDIA_FINAL)
else:
    print ("Aluno reprovado.")
