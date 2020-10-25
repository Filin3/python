def star(n):
    if n == 1: return "*"
    return star(n-1) + "*"

# print(star(int(input())))


x,y = (int(input("x, y: ")) for _ in range(2))

for X in range(x):
    mystr = ""
    mystr += star(y)
    print(mystr)