A = [int(i) for i in input().split()]


def quicksort(A):

    if len(A) <= 1:
        return A
    
    reference = A[len(A) // 2]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]


    return quicksort(small) + equal + quicksort(big)
    


print(quicksort(A))

