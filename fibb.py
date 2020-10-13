f = [0, 1]
try:
    x = int(input("Введите индекс числа фибб: "))
except ValueError:
    print("Ошибка")
    exit()
for i in range(2, x+1):
    f.append(f[i-1] + f[i-2])
print(f[x])