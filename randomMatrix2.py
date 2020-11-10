# import random
# xArr = []
# for i in range(3):
#     s = ""
#     xArr.append([])
#     xArr[i].append(100)
#     xArr[i].append(0)
#     for j in range(4):
#         el = random.randint(0, 100)
#         if xArr[i][0] > el:
#             xArr[i][0] = el
#         if xArr[i][1] < el:
#             xArr[i][1] = el
#         s += str(el) + " "
#     print(s)
#     print("elMin: {} elMax: {}".format(xArr[i][0], xArr[i][1]))

import random
for i in range(3):
    s = ""
    elMin = 100
    elMax = 0
    for j in range(4):
        el = random.randint(0, 100)
        if elMin > el:
            elMin = el
        if elMax < el:
            elMax = el
        s += str(el) + " "
    print(s)
    print("elMin: {} elMax: {}".format(elMin, elMax))