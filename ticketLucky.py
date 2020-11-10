import random
Sum = 0

while True:
    s1 = 0
    s2 = 0
    ticketNumber = ""
    for i in range(6):
        if i < 3:
            n = random.randrange(0,10)
            s1 += n
            ticketNumber += str(n)
        else:
            n = random.randrange(0,10)
            s2 += n
            ticketNumber += str(n)
    if s1 == s2:
        print(Sum)
        print(ticketNumber + " Lucky")
        break
    else:
        print(ticketNumber + " not lucky")
        Sum += 1