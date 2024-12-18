n, k = input().split(" ")
n = int(n)
k = int(k)


A = list(map(int, input().split()))


def quicksort(A):

    if len(A) <= 1:
        return A
    
    reference = A[len(A) // 4]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]

    return quicksort(small) + equal + quicksort(big)

A = quicksort(A)
B = [0] * k

for i in range(k):
    B[i] = str(A[i])    

print(" ".join(B))


