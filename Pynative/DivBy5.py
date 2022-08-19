#Iterate the given list of numbers and print only those numbers which are divisible by 5
list = []
i = 1
length = ""
print("Press enter on blank input to complete list")
while i == 1:
    takeElem = input("Input number: ")
    try:
        number = int(takeElem)
    except ValueError:
       # print("That's not an int or float!")
        break
    list.append(int(takeElem))
    length = len(list)
print("Old list:",list)
print("\n")

def check(list):
    newlist = []
    for i in range(length):
        if (list[i] % 5) == 0:
            print("Divisible by 5:", list[i])
            newlist.append(list[i])
        else:
            print("###################")
            print(list[i], "is not divisible by 5\n")
    print(newlist)
check(list)
