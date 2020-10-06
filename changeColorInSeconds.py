colorList = ["красный", "желтый", "белый", "синий", "зелёный", "голубой", "фиолетовый"]
sec = 5
pickedColor = 4
while sec < 147:
    if sec % 20 == 0:
        if len(colorList)-1 <= pickedColor:
            pickedColor = 0
        else:
            pickedColor += 1
    sec += 1
    #print(sec, pickedColor, colorList[pickedColor])    
print(sec, pickedColor, colorList[pickedColor])
