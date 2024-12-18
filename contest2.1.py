a = [i for i in input().split()]           # вводим данные 


def sumdig(c):

    
    d = 0
    for i in range(len(c)):
        d = d + c[i]

    return d

def sumdig2(b):

    b = str(b)
    c = [0] * len(b)
    for i in range(len(b)):
        c[i] = b[i]
    
    for i in range(len(c)):
        c[i] = int(c[i])   

    return sumdig(c)



for i in range(len(a)):             # каждый элемент массива представляем в виде цифр
    a[i] = list(map(int, str(a[i])))            


b = [0] * len(a)


for i in range(len(a)):

    if len(a[i]) > 1:
        b[i] = sumdig(a[i])
        
        while len(str(b[i])) > 1:
            b[i] = sumdig2(b[i])


for j in range(len(a)):
    if len(a[j]) == 1:

        b[j] = int(''.join(map(str, a[j])))


#print(b)

#for i in range(len(b)):
#    if b[i] < b[i + 1]:
#        b[i], b[i - 1] = b[i - 1], b[i]
    

def Quicksort(A):
    if len(A) <= 1:
        return A
    reference = A[len(A) // 2]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]
    return Quicksort(small) + equal + Quicksort(big)


print(Quicksort(b))

