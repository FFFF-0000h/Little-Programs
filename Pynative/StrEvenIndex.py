# Write a program to accept a string from the user and display characters that are present at an even index number

string = input("Enter any string/phrase: ")
length = len(string)

for i in range(0,length,2):
   print(string[i])

# slicee = string[0:length:2]
# for i in slicee:
    # print(i)
