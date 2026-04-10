# 2. WAP to rotate a list to the right by k positions, where k is an integer provided as input
# using list.
def rotate_list(lst, k):
    k = k % len(lst) 
    #rotated = #take last k element + first elements except last k
    rotated = lst[-k:] + lst[:-k]  
    print(rotated)

numbers = [1, 2, 2, 2, 4, 7, 3, 2, 1, 2, 4]
k = int(input("Enter positions for rotation: "))

rotate_list(numbers, k)
