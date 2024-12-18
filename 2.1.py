a = list(map(str, input().split()))
N = int(a[0])
a.pop(0)

for i in range(len(a)):
    a[i] = str(a[i])

for i in range(1, N + 1):
    if a.count(str(i)) == 0:
        print(i)
