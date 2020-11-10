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

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[j][i])