matrix = []

def getMatrixA(m):
    stepOne = m[0][0] * m[1][1] * m[2][2] + m[0][2] * m[1][0] * m[2][1] + m[2][0] * m[0][1] * m[1][2]
    stepTwo = m[0][2] * m[1][1] * m[2][0] + m[0][0] * m[1][2] * m[2][1] + m[2][2] * m[1][0] * m[0][1]
    result = stepOne - stepTwo
    if int(result) == result: result = int(result)
    return  result

for i in range(3):
    matrix.append([])
    for j in range(3):
        while True:
            try:
                matrix[i].append(float(input("Введите элемент Матрицы[{}][{}]: ".format(i+1, j+1))))
                break
            except ValueError:
                print("Введено недопустимое значение для: Матрицы[{}][{}]".format(i+1,j+1))

for i in range(3):
    s = ""
    for j in range(3):
        el = matrix[i][j]
        if int(el) == el: el = int(el) 
        s += str(el) + " "
    print(s)

print("A: " + str(round(getMatrixA(matrix), 4)))
