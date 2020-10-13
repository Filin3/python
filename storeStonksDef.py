def storeStonks(stonks, day):
    if day <= 1:
        return stonks
    print(day, stonks)
    return storeStonks(stonks * 2, day - 1)
print(storeStonks(200, 30))
