# Write a program to remove characters from a string starting from zero up to n and return a new string

#string = ""
word = input("Words? ")
amt = int(input("How many letters would you like to cut from the first? "))
def Rmv(amt, word):
    length = len(word)
    print("Original string is: ", word)
    if amt < length:
        word = word[amt:]
        print("\n")
        return word
    else:
        print("\n")
        return "\nCould not cut due to a known error, you either inputted a letter for amt or exceeded the amt compared to the word(s)"

print(Rmv(amt, word))
