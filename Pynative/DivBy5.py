#Iterate the given list of numbers and print only those numbers which are divisible by 5
list = []
takeElem = input("Enter number elements: ")
length = len(takeElem)
concat = ""
for i in range(length):
    Indexx = takeElem[i]
    list.append(Indexx)
print("\nList =",list)

for i in range(length):
    Indexx1 = list[i]
    Indexx2 = ""
    if list[i] == Indexx1:
        continue
    Indexx2 = list[i]
#print("\n List =", list)
print("\n")

def check(list):
    for i in list:
        if (list[i] % 5) == 0:
            print("Divisible by 5", list[i])
            print("\n")
#check(list)
