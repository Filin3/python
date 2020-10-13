colorList = ["красный", "желтый", "белый", "синий", "зелёный", "голубой", "фиолетовый"]
sec = 5
pickedColor = 4
while sec < 147 + 5:
    if sec % 20 == 0:
        pickedColor += 1
        if len(colorList) <= pickedColor:
            pickedColor = 0
    sec += 1
print("Цвет горит уже:", sec % 20)    
print(sec, pickedColor, colorList[pickedColor])
