# 4. WAP to count the frequency of each character in a given string and store the result in
# a dictionary.

def cal_freq(str):
    dist ={}
    for c in str:
        if c in dist:
            dist[c]+=1
        else:
            dist[c]=1
    return dist

text = input("Enter a String::")
dist = cal_freq(text)
print(dist)