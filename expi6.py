import datetime
start = datetime.datetime.now()

a = [12, 4, 2, 1, 23, 4, 3]


def quicksort(a):

    if len(a) <= 1:
        return a

    reference = a[len(a) // 4]


    small = [number for number in a if number < reference]
    equal = [number for number in a if number == reference]
    big = [number for number in a if number > reference]

    return quicksort(small) + equal + quicksort(big)

print(quicksort(a)) 
 
finish = datetime.datetime.now()

print(finish - start)

