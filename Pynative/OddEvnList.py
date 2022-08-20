# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

lst1 = []
lst2 = []
newlst = []
print("Press Enter twice to complete list")
while True:
    take1 = input("Enter list1 elements: ")
    try:
        number = int(take1)
    except ValueError:
        print("\n")
        break
    lst1.append(int(take1))
    print(lst1)

while True:
    take2 = input("Enter list2 elements: ")
    try:
        number = int(take2)
    except ValueError:
        print("\n")
        break
    lst2.append(int(take2))
    print(lst2)

for i in lst1:
    if (i % 2) != 0:
        newlst.append(i)
    else:
        continue

for i in lst2:
    if (i % 2) == 0:
        newlst.append(i)
    else:
        continue
print("New list =", newlst)
