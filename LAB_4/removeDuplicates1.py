# 1. WAP that removes all duplicate elements from a list without using set() and
# preserves the original order.



def remove_duplicates(numbers):
    num =[]
    for i in numbers:
        if i not in num:
            num.append(i)
            print(i, end=" ")


numbers=[1, 2, 3, 3, 3, 3, 3, 3, 3, 3]


remove_duplicates(numbers)


