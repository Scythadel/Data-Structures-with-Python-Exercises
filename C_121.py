b = []
while not EOFError:
    a = str(input("Enter standard input: "))
    b.append(a)

b.reverse()
print(b)