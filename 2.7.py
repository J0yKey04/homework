def most_frequent(data):

    counts = {}
    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = 0
    most_frequent_num = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent_num = num

    return most_frequent_num


data = list(map(int, input().split()))
most_frequent_num = most_frequent(data)
print(most_frequent_num) 
