list = []
y = int(input("Enter how many elements does your list have: "))
for i in range(y):
    x = int(input("Enter digits: "))
    list.append(x)

list.sort()
print("First element is: ", list[0], "and last element is: ", list[y-1])