from random import randint
def shuffle(data):
    for i in range(len(data) - 1):
        random_range = randint(0, len(data) - 1)
        if i == random_range:
            random_range = randint(0, len(data) - 1)
        data[i] = data[random_range]
    print(data)

shuffle([1,2,3,4])
    