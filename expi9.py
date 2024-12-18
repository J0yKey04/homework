a = [0] * 7

for i in range(0, 7, 2):
    a[i] = i

for i in range(1, 6, 2):
    a[i] = i

for i in range(len(a)):
    a[i] = str(a[i])


print(a)

print(a.count('4'))