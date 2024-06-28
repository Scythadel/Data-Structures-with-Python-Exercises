a = []
how_many = int(input("Enter how many elements in the list you want: "))
for i in range(how_many):
    elements = int(input("Enter the elements: "))
    a.append(elements)

a.sort()
for i in range(len(a) - 1):
    found = False
    if a[i] != a[i+1]:
        print("Yes all numbers are distinct")
        found = True
    elif a[i] == a[i+1]:
        print("No all numbers are not distinct")
    break

if IndexError:
    ""