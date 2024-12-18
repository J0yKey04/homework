A = [int(i) for i in input().split()]

def bubble(A):

    n = 1

    while n < len(A):

        for i in range(len(A) - n):

            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

        n += 1
        
    return A

print(bubble(A))
