n = int(input())
A = []
for i in range(n):
    A.append([0] * n)

for i in range(n):
    for j in range(n):
        if i > j:
            A[i][j] = n - i + j
        elif j == i:
            A[i][j] = n
b = []
for i in range(n):
    b.append(A[i][24])
for i in range(len(A)):
    print(*A[i])
print(min(b))