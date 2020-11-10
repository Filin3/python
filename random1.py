import random
a = []
for i in range(10):
    a.append(random.randint(1, 10))
print(a)

for i in range(len(a)-1):
    for k in range(1, len(a)-i):
        if a[k] < a[k-1]:
            z = a[k]
            a[k] = a[k-1]
            a[k-1] = z
print(a)