a = list(map(int, input().split()))
length = a[0]
width = a[1]


mas = [0] * width
for i in range(width):
   mas[i] = [0] * length

if length + width < 5:
    print(0)

elif length + width == 5:
    print(1)

else:
    mas[1][2] = 1
    mas[2][1] = 1


    for i in range(2, width, 1):
        for j in range(2, length, 1):
            mas[i][j] = mas[i - 2][j - 1] + mas[i - 1][j - 2]
        

    print(mas[width- 1][length - 1])

   
