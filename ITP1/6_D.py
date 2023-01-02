# 6_D.py

n, m = map(int, input().split())
a = [[]] * n
b = [0] * m
c = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(m):
    b[i] = int(input())

for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
    print(c[i])
