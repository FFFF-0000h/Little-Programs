# Write a Program to extract each digit from an integer in the reverse order
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits

num = input("Enter number: ")
length = len(num)
reverse = ""
def palin(num):
    for i in range(length):
        reverse = num[i::]
        print(reverse)
    print(reverse, end=" ")
palin(num)
