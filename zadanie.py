import math
def y(x):
    return (x ** 2) * math.exp(1 / x)

s = float(input())
n = float(input())
h = float(input())
print('x', '  y')
while s >= n:
    print(n, y(n))
    n += h
    n = round(n, 2)