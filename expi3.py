b = int(input())
b = str(b)
c = [0] * len(b)
for i in range(len(b)):
    c[i] = b[i]
    
for i in range(len(c)):
    c[i] = int(c[i])  

    print(type(c[i]), c[i])

print(c, type(c))