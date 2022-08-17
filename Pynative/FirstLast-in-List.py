# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False

list = []
print("###########################################################")
print("###########################################################")
print("Do you want a list of numbers or strings?")
print("1. Number\n2. String")
NumStrQuest = input()
if NumStrQuest == "1":
    takeElem = input("Enter numbers: ")
    length = len(takeElem)
    for i in range(length):
        list.append(int(takeElem[i]))
    print("\nList =",list)
print("\n")


if NumStrQuest == "2":
    takeElem = input("Enter strings: ")
    for i in takeElem:
        list.append(i)
    print("\nList =",list)
print("\n")

def check(list):
    for i in list:
        if list[0] == list[-1]:
            print("The first character is equal to the last character\nTrue")
            break
        else:
            print("The first character is not equal to the last character\nFalse")
            break
check(list)
