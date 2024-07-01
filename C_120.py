from random import randint
def shuffle(data):
    k = 0
    for i in data:
        random_range = randint(0, len(data) - 1)
        while k == random_range:
            random_range = randint(0, len(data) - 1)
        data[k] = data[random_range]
        k = k + 1
    print(data)

shuffle([1,2,3,4])
    