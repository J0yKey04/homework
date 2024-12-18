def unique_elements(s):

    unique_elements = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            unique_elements.append(s[i])
    return unique_elements

s = list(map(int, input().split()))


if len(s) > 1:
    a = unique_elements(s)
    print(a[0])
else:
    print(''.join(map(str, unique_elements(s))))

