myArr = []
for i in range(5):
    if i % 2 == 0:
        print()
        for x in range(3, 0, -1):
            if x == 2:
                myArr.append(x * 12 - 12)
                print(x * 12 - 12, end=" ")
            elif x == 1:
                myArr.append(x * 12 + 12)
                print(x * 12 + 12, end=" ")
            else: 
                myArr.append(x * 12)
                print(x * 12, end=" ")
    else:
        print()
        for x in range(3):
            if x == 0:
                print(str(myArr[2]) + str(myArr[1]), end=" ")
            else:
                print(6 // x, end=" ")
