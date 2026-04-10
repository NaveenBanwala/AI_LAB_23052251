#5 Write a Python program that takes two sets of integers as input and returns a new set
# containing all the elements that are common to both sets, but the common elements
# should be raised to the power of 2.

set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))

set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

common_elements = set1 & set2  # '&' gives intersection of two sets

squared_common = {x**2 for x in common_elements}

print("Common elements squared:", squared_common)
