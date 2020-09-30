def taskOne(p, s):
    if p < 15:
        p += 1
        s += 3
        return taskOne(p, s)
    else: 
        return s

def taskTwo(p, d):
    if d < 4:
        d += 1
        p -= 1
        if d == 2:
            p += 10
        return taskTwo(p, d)
    else:
        return p

def factor(count):    
    if count == 0:
        return 1
    else:
        print(count)
        return factor(count-1)*count

def choiceTask():
    choice = input("Задачи:\n1 - пошив пальто\n2 - магазин с пальто\n3 - факториал\nВыберите задачу: ")
    if choice == "1":
        print(taskOne(2, 0))
    elif choice == "2":
        print(taskTwo(2, 0))
    elif choice == "3":
        try:
            print(factor(int(input("Введите число для возведения в факториал: "))))
        except ValueError:
            print("Введенно некорректное значение")
            return choiceTask()
    else:
        return choiceTask()

choiceTask()