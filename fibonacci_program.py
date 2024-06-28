x = int(input("Enter how many elements in the fibonacci sequence: "))
fibonacci = [1, 1]
for i in range(x-2):
    fibonacci_next = fibonacci[i+1] + fibonacci[i]
    fibonacci.append(fibonacci_next)

print(fibonacci)