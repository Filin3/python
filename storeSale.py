goods = ["мясо", "конфеты", "конселярия", "чай", "кофе", "быт. химия", "памперсы"]
day = 1
for i in range(33):
    day += 1
    # if day > 6: 
    #     day = 0
print(goods[day%7])
#print(goods[day])