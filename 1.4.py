f = open('input.txt')
a = f.readline()
c = f.readline()
y = open('output.txt','w')
a = str(a) 
a = list(map(int, a.split()))
b = 0
d = 1
g = 0

c = str(c)
if (c == str('+')):
    for i in range(len(a)):
        b = b + a[i]
    y.write(str(b))

elif (c == str('*')):
    for i in range(len(a)):
        d = d * a[i]  
    y.write(str(d))

elif (c == str('-')):
    for i in range(len(a) - 1):
        g = g + a[i + 1]
    l = a[0] - g
    y.write(str(l))

else:
    print('Требуешь слишком многого(^)')

