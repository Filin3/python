# for i in range(100,1000):
#     s = str(i)
#     if (s[0] == s[2]):
#         print(s)

for i in range(1, 10):
    for j in range(10):
        for z in range(10):
            if i == z:
                print("{}{}{}".format(i,j,z))