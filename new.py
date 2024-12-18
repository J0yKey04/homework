a = int(input())

def fig(a):

    f = [0] * a 

    n = 0
    if a < 1:
        return 1
    
    for i in range(1, a + 1):
        if a % i == 0:
            f[i - 1] = i

            n += 1
        
        else: 
            f[i] = 0
    
    while (a - n) >= 1:
        f.remove(0) 
        n -= 1
    return f 
    f.remove(a)
    result = ' '.join(str(item) for item in f)

    return result


print(fig(a))
