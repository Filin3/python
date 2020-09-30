print("*Конвертор величин*\n1 - дециметр\n2 - километр\n3 - метр\n4 - миллиметр\n5 - сантиметр\nВыберите вашу величину")
choice = input()
print("Введите значение вашей величины")
lenght = input()

try:
    choice = int(choice)
    lenght = float(lenght)
except ValueError:
    print("Вы ввели не корректные значения")
    exit()

if choice >= 1 and choice <= 5:
    if lenght >= 0:
        if choice == 1: result = lenght / 10
        elif choice == 2: result = lenght * 1000
        elif choice == 3: result = lenght
        elif choice == 4: result = lenght / 1000
        elif choice == 5: result = lenght / 100
        if result == int(result):
            print(int(result))
        else:
            print(result)
    else:
        print("Значение данной величины не может быть меньше 0")
else:
    print("Вы ввели число не входящие в диапазон")
