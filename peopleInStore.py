people = ["девочка", "мальчик", "девушка", "парень", "женщина - одинокая QwQ"]
humanWorkWeek = 1
weekDay = 3
pickedHuman = 2

while people[pickedHuman] != "мальчик":
    weekDay += 1
    if weekDay != 6 and weekDay != 7:
        humanWorkWeek += 1
        if humanWorkWeek >= 5:
            humanWorkWeek = 1
            pickedHuman += 1
            if len(people) <= pickedHuman:
                pickedHuman = 0
    if weekDay >= 8:
        weekDay = 1
print(people[pickedHuman], weekDay)

    

