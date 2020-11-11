table = []

while True:
    try:
        x1 = int(input("Enter size of table: [*:X] -  "))
        x2 = int(input("Enter size of table: [X:*] -  "))
        if x1 > 0 and x2 > 0:
            break
        else: 
            raise ValueError
    except ValueError:
        # if x1 > 0: 
        #     break
        # else:
        #     print("Wrong [*:X] it can't be " + str(x1))
        # if x2 > 0: 
        #     break
        # else:
        #     print("Wrong [X:*] it can't be " + str(x2))

for i in range(x1):
    table.append([])
    for j in range(x2):
        table[i].append((i+1)*(j+1))

for i in range(len(table)):
    s = ""
    for j in range(len(table[i])):
        el = str(table[i][j])
        lastElLen = len(str(table[len(table)-1][j]))
        space = " " * (lastElLen-(len(el)-1))
        s += space + el
    print(s)

 #table 20x20 multiply