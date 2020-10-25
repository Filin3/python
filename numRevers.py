def reversNum(x,Str):
    if x == 0: return len(Str)-1
    return reversNum(x-1, Str)-1

Str = input()
r = ""
for i in range(len(Str)):
    r += Str[reversNum(i, Str)]

print(r)


