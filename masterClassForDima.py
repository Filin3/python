import math
while True:
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        break
    except ValueError:
        print("Введино не допустимое значение")

d = b**2-4*a*c
print("d: {}".format(d))
if d > 0:
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    if int(x1) == x1: x1 = int(x1)
    if int(x2) == x2: x2 = int(x2)
    print("x1: {}\nx2: {}".format(x1, x2))
elif d == 0:
    if int(x) == x: x = int(x)
    x = (-b+math.sqrt(d))/2*a
    print("x: {}".format(x))
else:
    print("Нет решения")