diff = 0
k = 0
b = [0]
a = []
for i in range(0, 90, 2):
    a.append(i)
    if a[k] - a[k-1] == 2:
        diff = diff + 2
        for j in range(b[len(b) - 1], 90):
            b.append(j + diff)
            break
        k = k + 1
    else:
        k = k + 1

print(b)