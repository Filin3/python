for i in range(1, 10):
    for x in range(10):
        for z in range(10):
            if i*x*z == 100 * i + 10 + z:
                print(i*x*z)