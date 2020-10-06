import math

def vlcV(r, h):
    return (h/3) * math.pi * (r*r)

try:
    r1,r2 = (float(input("Введите радиус: ")) for _ in range(2))
    h1,h2 = (float(input("Введите высоту: ")) for _ in range(2))
except ValueError:
    print("Ошибка")
    exit()

print(vlcV(r1, h1) + vlcV(r2, h2))