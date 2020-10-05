dayList = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
print("Введите день недели от 1 до 7")
try:
    day = int(input())-1
except ValueError:
    print("Вы ввели не число")
    exit()
if day >= 0 and day <= 6:
    print(dayList[day])
else:
    print("Вы ввели число в неверном диапозоне")
    
