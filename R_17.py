n = int(input("Enter number: "))
a = sum([i*i for i in range(n, 0, -1) if i % 2 != 0])
print(a)