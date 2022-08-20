# Write a program to find how many times substring appears in a given string.

string = input("Enter any string or sentence: ")
print(string)
countme = input("Which word/letter do you want to be counted?: ")
result = string.count(countme)
print(countme,"appears",result, "time(s)")
