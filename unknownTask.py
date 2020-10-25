def chi(a,x):
    return a*x
def Zn(b):
    return b+1
Sum = 0
x = float(input())
n = int(input())
a = x
b = x+1
Sum = a/b
for i in range(1,n):
    Sum += chi(a,x)/Zn(b)
a = chi(a,x)
b = Zn(b)
print(Sum)
# def superDef(x,i):
#     return (x**i)/x+i
# Sum = 0

# x = int(input())
# n = int(input())

# for i in range(1,n+1):
#     Sum += superDef(x,i)
# print(Sum)
