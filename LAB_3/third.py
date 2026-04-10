size = int(input("Enter size of array: "))
number = []

for i in range(size):
    number.append(int(input(f"Enter a number at index {i}: ")))

for i in range(size):
    print(f"Index {i}:", number[i])

# Correct initialization
largest = number[0]
secondL = float('-inf')

for i in number:
    if i > largest:
        secondL = largest
        largest = i
    elif i > secondL and i != largest:
        secondL = i

print("Second largest is:", secondL)
