for k in range(4):
    r = ""
    z = 16
    for i in range(4):
        r += str(z) + " "
        z //= 2 
    print(r)