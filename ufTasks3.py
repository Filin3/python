x = ["aaabb", "caca", "dabc", "acc", "abbba"]
s = []
for i in range(len(x)):
    if x[i].count("c") != 0:
        s.append(x[i])
print(", ".join(s))