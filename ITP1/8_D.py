# 8_D.py

s = input()
p = input()

for i in range(len(s)):
    for j in range(len(p)):
        if s[(i + j) % len(s)] != p[j]:
            break
    else:
        print("Yes")
        break
else:
    print("No")
