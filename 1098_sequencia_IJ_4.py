##entrada
I = 0
A = 1
B = 2
C = 3
i = 0

##processamento
while True:
    if i > 2:
        break
    if i == 0:
        print("I=%d J=%d" % (I, A)) # saida
        print("I=%d J=%d" % (I, B))
        print("I=%d J=%d" % (I, C))
        
    if i == 2:
        print("I=%d J=%d" % (I, A)) # saida
        print("I=%d J=%d" % (I, B))
        print("I=%d J=%d" % (I, C))
        
    elif i > 0 and i < 2:
        print("I=%.1f J=%.1f" % (I, A)) # saida
        print("I=%.1f J=%.1f" % (I, B))
        print("I=%.1f J=%.1f" % (I, C))
    I += 0.2
    A += 0.2
    B += 0.2
    C += 0.2
    i = I
    
