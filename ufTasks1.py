x = ["aaabb", "caca", "dabc", "acc", "abbba"]
s = []
for i in range(len(x)):
    s.append(x[i].count("a"))
print(s)