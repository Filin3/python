s = ""
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            s += "*"
        elif j == 0 or j == n-1: 
            s+= "*"
        elif i == j:
            s += "*"
        elif i == n-1-j:
            s += "*"
        else:
            s += " "
    print(s)
    s = ""