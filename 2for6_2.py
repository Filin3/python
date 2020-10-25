s = ""
k = 0
for i in range(3):
    for j in range(4):
        x = input("Введите элемент {} строкой и {} столбцом: ".format(i+1, j+1))
        s += x
    s += "\n"
print(s)