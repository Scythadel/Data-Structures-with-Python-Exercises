a = [1,2,3]
b = int(input("Enter input: "))
try:
    for i in range(4):
        a[i] = b
    print(a)
except IndexError:
    print("Don't try to buffer overflow attacks in Python!")