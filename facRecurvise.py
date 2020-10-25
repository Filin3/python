try:
    n = int(input("Введите n: "))
except ValueError:
    exit()

def fac(n):
    if n == 0: return 1
    return fac(n-1)*n

if n >= 0 and n <= 15:
    print(fac(n))
else:
    print("Неверный диапозон n")
