def f(x, y, z):
    s = 0
    for i in range(x, y):
        s += 1 / (i ** z)
    return s

print((f(1, 5, 1) + f(1, 3, 2)) / 2)