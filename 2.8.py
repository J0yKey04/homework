def quicksort(A):

    if len(A) <= 1:
        return A
    
    reference = A[len(A) // 2]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]


    return quicksort(small) + equal + quicksort(big)

def find_median(n, lst):

    mid = n // 2
    return lst[mid]

n = int(input())
lst = list(map(int, input().split()))

print(find_median(n, quicksort(lst)))

# а как еще отсортировать если не с помощью сортировки????)
