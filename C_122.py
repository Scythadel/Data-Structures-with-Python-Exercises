def dot_product(a: list, b: list):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

print(dot_product([1,2,3], [1,2,3]))

