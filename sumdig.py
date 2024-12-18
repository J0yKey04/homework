a = int(input())


def sumdig(a):

    a = str(a)
    a = list(map(int, a))
    b = 0
    for i in range(len(a)):
        b = b + a[i]

    return b



print(sumdig(a))

