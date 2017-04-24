##entrada
x = int(input())
i = 1
a, b = 0, 1
print(a, end=" ")
i += 1
##processamento
while i <= x:
    while i < x:
        print(b, end=" ")
        a, b = b, a + b
        i += 1
    if i == x:
        print(b)
        i += 1
