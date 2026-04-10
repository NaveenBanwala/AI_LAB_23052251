# 2. Area Calculator: Write a Python function that calculates the area of different shapes
# (triangle, square, rectangle, and circle). The function should accept the necessary
# dimensions as arguments and return the corresponding area.


import math

def calculate_area(shape, **kwargs):
    shape = shape.lower()

    print(kwargs)
    
    if shape == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        if base is None or height is None:
            return "Error: Provide base and height for triangle."
        return 0.5 * base * height
    
    elif shape == "square":
        side = kwargs.get("side")
        if side is None:
            return "Error: Provide side length for square."
        return side * side
    
    elif shape == "rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        if length is None or width is None:
            return "Error: Provide length and width for rectangle."
        return length * width
    
    elif shape == "circle":
        radius = kwargs.get("radius")
        if radius is None:
            return "Error: Provide radius for circle."
        area= math.pi * radius * radius
        return area
    
    else:
        return "Error: Unknown shape."

# Example usage
print("Triangle area:", calculate_area("triangle", base=5, height=10))
print("Square area:", calculate_area("square", side=4))
print("Rectangle area:", calculate_area("rectangle", length=5, width=3))
area = calculate_area("circle", radius=7)
print(f"Circle area: {area:.3f}")

