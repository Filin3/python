weekDays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
colorList = ["красный", "синий", "желтый", "зелёный", "оранжевый", "розовый", "чёрный"]

dayIndex = 6
colorIndex = 0

while colorList[colorIndex] != "чёрный":
    colorIndex += 1
    dayIndex += 1
    if len(weekDays) <= dayIndex:
        dayIndex = 0
    if len(colorList) <= colorIndex:
        colorIndex = 0
print(colorList[colorIndex], weekDays[dayIndex]) 

