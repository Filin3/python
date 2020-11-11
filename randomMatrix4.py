#fil9

# import random
# matrix = []

# def showMatrix(m, size):
#     s = ""
#     for i in range(len(m)):
#         s += str(m[i]) + " "
#         if (i+1) % size == 0: s += "\n"
#     return s

# for i in range(4*3):
#     matrix.append(random.randint(0,10))

# print(showMatrix(matrix, 4))

# for i in range(len(matrix)-1):
#     for k in range(1, len(matrix)-i):
#         if matrix[k] < matrix[k-1]:
#             z = matrix[k]
#             matrix[k] = matrix[k-1]
#             matrix[k-1] = z

# print(showMatrix(matrix, 4))

#teacher
import random
s = []
m = ""
for i in range(3):
    m = ""
    for j in range(4):
        a = random.randint(0, 10)
        m += str(a) + " "
        s.append(a)
    print(m)
print()
for i in range(len(s)-1):
    for k in range(1, len(s)-i):
        if s[k] < s[k-1]:
            s[k], s[k-1] = s[k-1], s[k]
m = ""
z = 0
for i in range(3):
    m = ""
    for j in range(4):
        m += str(s[z]) + " "
        z+=1
    print(m)