
n = int(input())


def boom(n):
    l = 0
    for i in range(n, 0, -1):
       
        if n == 2:
            return 1 + l
        elif n == 3:
            return 1 + l
        elif n == 4:
            return 2 + l
        elif n == 5:
            return 3 + l
        elif n == 6:
            return 2 + l
        elif n == 7:
            return 3 + l
        elif n == 8:
            return 3 + l
        elif n == 9:
            return 2 + l 
        elif n == 10:
            return 3 + l
        
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n -= 1
        if n <= 0:
            return l

        
        l += 1
        print(n)


#def nil(n):
#    l = 0
 #   while n >= 0:
  #      
   # 
    #    if n % 3 == 0:
     #       n = n // 3
      #  elif n % 2 == 0:
       #     n = n // 2
        #else:
         #   n -= 1
        
      #  l += 1
    #return l - 1

print(boom(n))

