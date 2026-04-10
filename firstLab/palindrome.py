# 2. Write a Python program to check whether a given input (word or number) is a palindrome.



def checkPalindrome(input):
    # newStr=input[::-1]

    return input == input[::-1]


input = "121"

print(checkPalindrome(input))
