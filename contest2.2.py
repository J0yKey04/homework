vwv = list(map(int, input().split()))


print(-1, end = " ")


for k in range(1, len(vwv)):
    
    dig = -1
    h = vwv[k]
    k -= 1
    
    while k + 1:
        
        if (vwv[k] >= h and dig < k):
            dig = k
        
        k -= 1
    
    print(dig, end=" ")

