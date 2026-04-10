# 7. WAP to find the longest substring of a given string where all characters are unique.
# Return both the substring and its length.

s = input("Enter a string: ")

char_set = set()
start = 0
max_len = 0
longest_substring = ""

for end in range(len(s)):
    while s[end] in char_set:
        char_set.remove(s[start])
        start += 1

    char_set.add(s[end])

    if end - start + 1 > max_len:
        max_len = end - start + 1
        longest_substring = s[start:end+1]

print("Longest substring with unique characters:", longest_substring)
print("Length:", max_len)
