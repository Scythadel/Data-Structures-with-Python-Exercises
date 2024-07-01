def check(a: int, b = int, c = int):
    if a + b == c or a == b - c or a * b == c:
        return True
    return False

print(check(5,6,7))