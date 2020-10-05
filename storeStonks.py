stonks = [200]
sum710 = 0
sumM = 0
for i in range(1, 30):
    stonks.append(stonks[i-1] * 2)
    sumM += stonks[i]
    if i >= 6 and i <= 9:
        sum710 += stonks[i]
print("Сумм за месяц:", sumM, "\nСумма за 7,8,9,10:", sum710, "\n7:", stonks[6], "\n8:", stonks[7], "\n9:", stonks[8], "\n10:", stonks[9])


