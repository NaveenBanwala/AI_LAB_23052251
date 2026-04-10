# 5. Write a Python program to generate the Fibonacci series up to a
# specified number of terms. Use a while loop and branching to
# implement the logic.

# Fibonacci Series using while loop and branching

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
