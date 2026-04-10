# Question 1 : Create a program that takes two numbers as input, adds them, and
# prints the result. Ensure they handle cases where the inputs might be
# strings (requiring type conversion).

x= input("Enter first number ->")
y=input("Enter Second number->")

answer = float(x) + float(y)
print("Result ->", answer)