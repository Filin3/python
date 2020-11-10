tal = 1770
l = tal//31
b = tal//21

for x in range(l+1):
    for y in range(b+1):
        if 31*x+21*y == tal:
            print("L: {} B: {}".format(x,y))
