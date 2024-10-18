n = int(input())
b = int(input())
c = int(input())
y = 0
n = list(map(int, list(str(n))))


for i in range(len(n)):
    y = n[i] * b ** (len(n) - i - 1) + y


i = 0
li = [] 
while y > 0:

    l = y % c
    y = y // c
    i += 1
    li.append(l)

li.reverse()

print(''.join(map(str, li)))

