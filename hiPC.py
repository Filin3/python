print("Здравствуйте, я пк. Как вас зовут?")
name = input()
print("Очень приятно, " + name)
print("Сколько вам лет?")
age = int(input())
if age < 30: 
    print("Я старше вас на", 30 - age)
elif age > 30:
    print("Я младше вас на", age - 30)
else:
    print("Мы одногодки")
while True:
    print("Как у вас дела?")
    answer = input()
    if answer.lower() == "хорошо":
        print("Я очень рад за вас!")
        break
    elif answer.lower() == "плохо":
        print("pat pat")
        break
    else:
        print("Я вас не понял!")