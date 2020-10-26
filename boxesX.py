a = 185//16
b = 185//17
c = 185//21
for x in range(a+1):
    for y in range(b+1):
        for z in range(c+1):
            if 16*x+17*y+21*z == 185:
                print("16 кг: {} 17 кг: {} 21 кг: {}".format(x,y,z))
