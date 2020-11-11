import random
arr = []
for i in range(3):
    arr.append([])
    for j in range(4):
        arr[i].append(random.randint(0, 100))

s = ""
for i in range(len(arr)):
    for j in range(len(arr[i])):
        s += str(arr[i][j]) + " "
    s += "\n"
print(s)


for j in range(len(arr[0])):
    # s = ""
    Min = 100
    Max = 0
    for i in range(len(arr)):
        el = arr[i][j]
        if Min > el: Min = el
        if Max < el: Max = el
        # s += str(el) + " "
    print("Min: {} Max: {}".format(Min, Max))
    # print(s)
