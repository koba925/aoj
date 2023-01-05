# 7_C.py

maxr, maxc = [int(e) for e in input().split()]
m = [[]] * maxr
for i in range(maxr):
    m[i] = [int(e) for e in input().split()]

ct = [0] * maxc
for i in range(maxr):
    rt = 0
    for j in range(maxc):
        print(m[i][j], end=" ")
        rt += m[i][j]
        ct[j] += m[i][j]
    print(rt)

gt = 0
for j in range(maxc):
    print(ct[j], end=" ")
    gt += ct[j]
print(gt)
