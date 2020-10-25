z = 0
Sum = 0
for k in range(4):
    r = ""
    for i in range(5):
        z += 1
        r += str(z) + " "
        Sum += z
    print(r)
print(str(Sum) + "\n")

z = 21
Sum = 0
for k in range(4):
    r = ""
    for i in range(5):
        z -= 1
        r += str(z) + " "
        Sum += z
    print(r)
print(Sum)