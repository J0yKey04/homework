n = int(input())


def boom(n):
    l = 0
    for i in range(n, 0, -1):

        l += 1

        if n // 3:
            n = n // 3
        elif n // 2:
            n = n // 2
        else:
            n -= 1
        if n <= 0:
            return l + 1

    


print(boom(n))
