numero = int(input())

while numero > 0:
    palavra = input()
    palavraAux = ""
    tamanho = 0
    # Passa pra 3
    while tamanho < len(palavra):
        numAscii = ord(palavra[tamanho])
        if (numAscii >= 65 and numAscii <= 90)or(numAscii >= 97 and numAscii <= 122):
            letra = chr(numAscii + 3)
            palavraAux += letra
        else:
            palavraAux += palavra[tamanho]
        tamanho += 1

    # Inversão da string
    palavraAux = palavraAux[::-1]

    parteInicial = palavraAux[:len(palavraAux)//2]
    parteFinal = palavraAux[len(palavraAux)//2:]
    tamFinal = 0
    
    resultado = parteInicial
    # Passa pra -1
    while tamFinal < len(parteFinal):
        numAscii = ord(parteFinal[tamFinal])
        letra = chr(numAscii- 1)
        resultado += letra
        
        tamFinal += 1

    print(resultado)
    
    numero -= 1
