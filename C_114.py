a = []
how_many = int(input("Enter how many elements in the list you want: "))
for i in range(how_many):
    elements = int(input("Enter the elements: "))
    a.append(elements)

for j in a:
    found = False
    for k in range(a[1], len(a) - 2):
        if j != a[k]:
            if (j*a[k]) % 2 != 0:
                print("Yes there is a distinct pair of values")
                found = True
                break
            else:
                print("No there is no distinct pair of values")
    if found:
        break