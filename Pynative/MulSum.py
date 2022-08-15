## Given two integer numbers, return their product only if the product is equal to or lower than 1000, else return their sum

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

def MulSum(num1,num2):
    product = num1 * num2
    sum = num1 + num2
    if product <= 1000:
        return product
    else:
        return sum

print(MulSum(num1,num2))
