colorList = ["красный", "желтый", "белый", "синий", "зелёный", "голубой", "фиолетовый"]
sec = 5
pickedColor = 4
for i in range(147):
    if i % 20 == 0:
        pickedColor += 1
    if len(colorList) <= pickedColor:
        pickedColor = 0

print(colorList[pickedColor])
print(i)