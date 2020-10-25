p = 200
Sum = 200
for i in range(2, 31):
    p *= 2
    Sum += p
    if i >= 7 and i <= 10:
        print(i,p)
print("Сумма прибыль {}".format(Sum))  