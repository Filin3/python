fbbList = [0,1]
def fbb(i):
    print(i, fbbList)
    if i <= 1:
        return fbbList[len(fbbList) - 1]
    else:
        fbbList.append(fbbList[len(fbbList)-2] + fbbList[len(fbbList)-1])
        return fbb(i-1)
print(fbb(25))