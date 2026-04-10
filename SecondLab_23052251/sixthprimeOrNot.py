# 6. Create a program that takes user input and checks whether the
# entered number is a prime number or not. Utilize a for loop and
# branching statements.

# Program to check whether a number is prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
