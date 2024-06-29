diff = 2
b = [0]
a = []
for i in range(0, 90, 2):
    a.append(i)
    if a[i] - a[i-1] == 2:
        diff = diff + 2
        for j in range(2, 92, diff):
            b.append(j)
    else:
        continue

print(b)