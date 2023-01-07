# 7_D.py

n, m, l = [int(e) for e in input().split()]


def mat_init(n, m):
    return [[0 for e in range(m)] for e in range(n)]


def mat_read(n, m):
    a = mat_init(n, m)
    for i in range(n):
        a[i] = [int(e) for e in input().split()]
    return a


def mat_mul(a, b):
    n = len(a)
    m = len(b)
    l = len(b[0])

    c = mat_init(n, l)
    mat_print(c)
    for i in range(n):
        for j in range(l):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]

    return c


def mat_print(a):
    for r in a:
        print(*r)


a = mat_read(n, m)
b = mat_read(m, l)
mat_print(a)
mat_print(b)

mat_print(mat_mul(a, b))
