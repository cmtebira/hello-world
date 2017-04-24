##entrada
quant_casos = int(input())
quant_led = 0
z = 1
i = 0

##processamento
while z <= quant_casos:
    numero = input()
    lista_numeros = list(numero)
    tamanho_numero = len(lista_numeros)
    while i < tamanho_numero:
        caracter = lista_numeros[i]
        if int(caracter) == 0:
            quant_led += 6
        elif int(caracter) == 1:
            quant_led += 2
        elif int(caracter) == 2:
            quant_led += 5
        elif int(caracter) == 3:
            quant_led += 5
        elif int(caracter) == 4:
            quant_led += 4
        elif int(caracter) == 5:
            quant_led += 5
        elif int(caracter) == 6:
            quant_led += 6
        elif int(caracter) == 7:
            quant_led += 3
        elif int(caracter) == 8:
            quant_led += 7
        elif int(caracter) == 9:
            quant_led += 6
        i += 1

##saida

    print("%d leds" % quant_led)
    i = 0
    quant_led = 0
    z += 1
