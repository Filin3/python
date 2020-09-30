try:
    print("Введите месяц:")
    m = int(input())-1
    print("Введите число:")
    d = int(input())
except ValueError:
    print("Введены некорректные данные")
    exit()

mArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m <= 11 and m >= 0 and mArr[m] >= d and mArr[m] >= 0: 
    result = d
    for i in range(12):
        if m > i:
            result += mArr[i]
        else:
            break
    print(result)
else:
    print("Некорректный месяц или число")
