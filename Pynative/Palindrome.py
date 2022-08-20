# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

num = input("Enter number: ")
length = len(num)
reverse = ""
def palin(num):
    i = 0
    while i < length:
        reverse = num[::-1]
        i += 1
        num = int(num)
        reverse = int(reverse)
        if num == reverse:
            print(reverse, "is a Palindrome!")
            break
        else:
            print(reverse)
            break
palin(num)
