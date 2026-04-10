# 2. Write a program that calculates the area of a rectangle using user-
# input length and width, and then compare it with the area of a

# square with side length half of the rectangle's width.

width= float(input("Enter width of rectangle:"))
length= float(input("Enter length of rectangle:"))

area = width * length
print(area)

squareSide = width/2

areaSq = squareSide * squareSide

if areaSq == area :
    print("Both equal")
elif areaSq < area:
    print("Area of Rectangle is more")
else :
    print("Square area is more")


