size = int(input())
xIndex = 0
for x in range(size):
    s = "*"
    xIndex += 1
    for y in range(1, size):
        if x == 0 or x == size-1:
            s += "*"
            continue
        if len(s) == xIndex:
            s += "*"
        elif size - len(s) == xIndex:
            s += "*"
        else:
            s += " "
    print(s + "*")
     