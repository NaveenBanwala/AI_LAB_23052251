#3. Write a program that checks whether a given number is prime or not.

def checkPrimeOrNot(x):
    if x <= 1:
        return False

    for y in range(2, (x // 2) + 1):
        if x % y == 0:
            return False

    return True

print(checkPrimeOrNot(int(input("Enter a number"))))
