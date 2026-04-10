# // 5. WAP to find the first non-repeating character in a string. If all characters repeat,
# // return “None”.

def find_nrc(c):
    noon_repeat ={}
    for i in c:
        if i in noon_repeat:
            noon_repeat[i] += 1
        else:
            noon_repeat[i] = 1

    for key, value in noon_repeat.items():
            if value == 1:
                return key

    return "None"


print(find_nrc(input("Enter a String::")))