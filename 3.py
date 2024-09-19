a = list(map(int, input().split()))
b = 1
for i in range(len(a)):
    b = b * a[i]

b = b ** (1/len(a))

print(b)

