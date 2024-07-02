def factors(n):
    list_k = []
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
            list_k.append(k)
        k = k + 1
    if k * k == n:
        yield k
        list_k.append(k)

print(factors(100))