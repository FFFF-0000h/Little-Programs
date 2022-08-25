# Write a Program to extract each digit from an integer in the reverse order
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits

number = int(input("Enter number: "))
def palin(number):
    print("Given number", number)
    while number !=  0:
        # get the last digit
        digit = number % 10
        # remove the last digit and repeat the loop
        number = number // 10
        print(digit, end=" ")
    print("\n")
palin(number)
