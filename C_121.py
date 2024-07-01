b = []
while 0 == 0:
    try:
        a = str(input("Enter standard input: "))
        b.append(a)
    except EOFError:
        b.reverse()
        print(b)