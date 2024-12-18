boys = list(map(int, input().split()))

ans = [0] * len(boys)


for k in range(len(boys)):

    fr = 0
    ind = k
    
    while True:
            
            found_fr = 0
            
            for i in range(ind + 1, len(boys)):
                
                if boys[i] > boys[ind]:  
                    
                    fr += 1
                    ind = i
                    found_fr = 1
                    break
            
            if found_fr == 0:
                break
    
    ans[k] = fr


for i in range(len(ans)):
    print(ans[i], end = " ")

print()

