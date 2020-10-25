import math

def sqrt(x):
    return math.sqrt(x)

Sum = 0
n = int(input())
x = float(input())

for i in range(n):
    Sum = sqrt(x)
    x += Sum
print(Sum)