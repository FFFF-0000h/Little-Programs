# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False

list = []
print("###########################################################")
print("###########################################################")
takeElem = input("Enter elements: ")
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
