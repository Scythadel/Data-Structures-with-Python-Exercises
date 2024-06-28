from random import randrange
a = []
def choice(data):
    for i in range(5):
        a.append(data)

    b = randrange(len(a) - 1)
    print(a[b])