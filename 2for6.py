matrix = ""
for k in range(1, 4):
    line = ""
    for i in range(1, 5):
        line += input("\"i: {} j: {}\": ".format(k, i)) + " "
    matrix += line + "\n"
print(matrix)
