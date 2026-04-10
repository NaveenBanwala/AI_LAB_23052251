# 4. Write a program that takes a list of words and returns a dictionary that maps each
# word to its frequency in the list.

words = input("Enter words separated by spaces: ").split()


word_freq = {} #Empty Dictionary

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("frequencies:", word_freq)
