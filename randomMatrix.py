import random
elMin = 100
elMax = 0
for i in range(3):
    s = ""
    for j in range(4):
        el = random.randint(0, 100)
        if elMin > el:
            elMin = el
        if elMax < el:
            elMax = el
        s += str(el) + " "
    print(s)
print("elMin: {} elMax: {}".format(elMin, elMax))