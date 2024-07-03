def divide_till_two(x: int):
    count = 0
    if x <= 2:
        raise ValueError("Value is less than or equal to two")
    while x >= 2:
        x = x / 2
        count = count + 1
    return count

print(divide_till_two(1))
