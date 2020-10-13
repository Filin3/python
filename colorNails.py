weekDays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
colorList = ["красный", "синий", "желтый", "зелёный", "оранжевый", "розовый", "чёрный"]

colorIndex = 0
dayIndex = 6

while colorIndex < 6:
    colorIndex += 1
    dayIndex += 1
    #if colorIndex == 7:
    if len(weekDays) <= dayIndex:
        dayIndex = 0
    #if dayIndex == 7:
    if len(colorList) <= colorIndex:
        colorIndex = 0
print(colorList[colorIndex], weekDays[dayIndex]) 

