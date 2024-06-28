duplicate_list = []
x = int(input("How many values do you want to be considered?: "))
for i in range(x):
    y = int(input("Enter the next value: "))
    duplicate_list.append(y)

duplicate_list.sort()

for j in range(x):
    if duplicate_list[j] == duplicate_list[j+1]:
        duplicate_list.remove(duplicate_list[j])
    else:
        continue

print(duplicate_list)