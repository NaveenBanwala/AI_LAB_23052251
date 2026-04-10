#Code for second Smalelst and largest

def secondLargest(L):
    largest=L[0]
    secondL =L[0]
    smallest = L[0]
    secondSmallest = L[0]
    for i in L:
        if i >largest:
            secondL =largest
            largest=i
        elif i >secondL and i!=largest:
            secondL = i
    return secondL

lst = [1,2,4]
print(secondLargest(lst))
