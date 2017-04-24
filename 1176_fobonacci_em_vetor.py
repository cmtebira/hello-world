##entrada
T = int(input())
contador = 1

##processamento
while contador <= T:
    N = int(input())
    fibo_ini = [0,1]
    num_anterior = 0
    num_posterior = 1
    pos = 0
    while pos <= N:
        novo_numero = num_anterior + num_posterior
        fibo_ini.append(novo_numero)
        num_temp = novo_numero
        num_anterior = num_posterior
        num_posterior = num_temp
        pos += 1
    print('Fib(%d) = %d' %(N, fibo_ini[N]))
    contador += 1
    
