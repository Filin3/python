def fac(n):
    if n == 0: return 1
    return fac(n-1)*n

S = 0
for i in range(2,17):
    if i % 2 == 0:
        S+=fac(i)
print(S)