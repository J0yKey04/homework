n, k = input().split(" ")

n = int(n)
k = int(k)

put_data = list(map(int, input().split()))


def insertion_sort(A):


    for i in range(1, len(A) - 1):
        if A[0] > A[i]:
            A[0], A[i] = A[i], A[0]
        
