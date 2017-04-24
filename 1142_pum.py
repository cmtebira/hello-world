##entrada
N = int(input())
x = 1
y = 2
z = 3
w = "PUM"
i = 1

##processamento
while i <= N:
##    print("%s", "%s", "%s", "%s" % (x, y, z, w))
    print(x, end=" ")
    print(y, end=" ")
    print(z, end=" ")
    print(w)
    x += 4
    y += 4
    z += 4
    i += 1
