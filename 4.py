f = open('input.txt')
a = f.readline()
c = f.readline()
a = str(a) 
a = [a.split()]

for i in range(len(a)):
    a[i] = int(a[i])

c = str(c)
c = c.split()


print(a, c)



