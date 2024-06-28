sum = 0
squares = []
n = int(input("Enter number: "))
for i in range(n, 0, -1):
    if i % 2 != 0:
        squares.append(i*i)

for k in squares:
    sum = sum + k

print(sum)