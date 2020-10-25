def part1(a,x):
    if a == 0: return x**2
    return part1(a-1, x)*x**2
def part2(b,x):
    if b == 0: return x**2 + 2
    return part2(b-1, x)*2*x**2

x = float(input())
n = int(input())

Sum = 1
for i in range(n-1):
    Sum += part1(i,x)/part2(i,x)
print(Sum)
