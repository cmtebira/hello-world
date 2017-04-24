##entrada
I = 0
A = 1
B = 2
C = 3
i = 0

##primeiros valores inteiros (I == 0)
print("I=%d J=%d" % (I, A)) # saida
print("I=%d J=%d" % (I, B))
print("I=%d J=%d" % (I, C))

##processamento antes de 1
while i < 0.8:
    I += 0.2
    A += 0.2
    B += 0.2
    C += 0.2
    i = I
    print("I=%.1f J=%.1f" % (I, A)) # saida
    print("I=%.1f J=%.1f" % (I, B))
    print("I=%.1f J=%.1f" % (I, C))

##valores inteiros (I == 1)
I = 1
A = 2
B = 3
C = 4
i = 1
print("I=%d J=%d" % (I, A)) # saida
print("I=%d J=%d" % (I, B))
print("I=%d J=%d" % (I, C))

##processamento antes de 2
while i < 1.6:
    I += 0.2
    A += 0.2
    B += 0.2
    C += 0.2
    i = I
    print("I=%.1f J=%.1f" % (I, A)) # saida
    print("I=%.1f J=%.1f" % (I, B))
    print("I=%.1f J=%.1f" % (I, C))

##valores inteiros (I == 2)
I = 2
A = 3
B = 4
C = 5
i = 2
print("I=%d J=%d" % (I, A)) # saida
print("I=%d J=%d" % (I, B))
print("I=%d J=%d" % (I, C))
    
