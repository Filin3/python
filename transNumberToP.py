import math
res = []
def transNum(num, p):
    if num < p: return res.append(num)
    res.append(num%p)
    return transNum(math.trunc(num/p), p)

num = int(input())
p = int(input())

transNum(num, p)
res.reverse()
r = ""
for i in range(len(res)):
    r += str(res[i])
print(r)