n = int(input())

def ph(n):

    if n <= 1:
        return n
    else:
        return ph(n - 1) + ph(n - 2)
    

print(ph(n))

