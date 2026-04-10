
def s_smallest(S):
    s = S[0]
    sL= S[0]
    for i in S:
        if i < s:
            s = sL
            sL = i
        elif  i >sL and i!=s:
            s =i
    return sL        

lst=[1,3,45,2]            
print("Second Smallest ", s_smallest(lst))