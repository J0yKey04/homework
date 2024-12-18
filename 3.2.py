a = int(input())
i = 2

def simple(a, i):
    

    while a > 1 and a >= i:
    
        if a % i == 0:
            a = a // i
            print(i)
            return simple(a, i) 

        else:
            return simple(a, i + 1)
        

print(simple(a, i))


