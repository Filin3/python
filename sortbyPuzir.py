a = [3, 1, 2, 4, 8, 2, 0, 7]

for i in range(len(a)-1):
    for k in range(1, len(a)-i):
        if a[k] < a[k-1]:
            z = a[k]
            a[k] = a[k-1]
            a[k-1] = z
print(a)