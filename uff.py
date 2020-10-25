def part1(a,x):
    return a*x**2
def part2(b,x):
    return 2*x**2*b

x = float(input())
n = int(input())

Sum = 1
a = x**2
b = x**2 + 2
Sum += a/b
for i in range(2, n):
    Sum += part1(a,x)/part2(b,x)
    a = part1(a,x)
    b = part2(b,x)
print(Sum)


 





print("Я люблю Кирилла!")