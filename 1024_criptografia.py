##entrada
quant_testes = int(input())
z = 1

##processamento
while z <= quant_testes:
    palavra = input()
    chave1 = 3
    pos = 0
    nova_palavra = ""
    while pos < len(palavra) : # primeira passada
        letra = palavra[pos]
        num_ascii = ord(letra)
        if 65 <= num_ascii <= 90 or 97 <= num_ascii <= 122:
            novo_ascii = num_ascii + chave1
            nova_letra = chr(novo_ascii)
            nova_palavra += nova_letra
        else:
            nova_palavra += letra
        pos += 1
    palavra_invertida = nova_palavra [::-1] # segunda passada
    chave2 = 1
    pos = 0
    metade = int(len(palavra_invertida)/2)
    palavra_final = ""
    while pos < len(palavra_invertida) : # terceira passada
        letra = palavra_invertida[pos]
        if pos < metade:
            palavra_final += letra
        else:
            num_ascii = ord(letra)
            novo_ascii = num_ascii - chave2
            nova_letra = chr(novo_ascii)
            palavra_final += nova_letra
        pos += 1

##saida        
    print(palavra_final)
    z += 1
