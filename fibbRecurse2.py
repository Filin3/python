def f(n):
    if n == 1 or n == 2: return 1
    return f(n-1) + f(n-2)
s = 0
for i in range(1,11):
    print(f(i))
    s += f(i)
print(s)