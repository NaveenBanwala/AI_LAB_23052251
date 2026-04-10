#1. Write a Python program to count vowels and consonants in a given string.

# Example:
# Input → "Hello World"
# Output → Vowels: 3, Consonants: 7

def get_VC(text):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    text = text.lower()

    for char in text:
        if 'a' <= char <= 'z':
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count


input_text = "Naveen Banwala"
v, c = get_VC(input_text)

print(f"Input String: {input_text} -> Vowels: {v}, Consonants: {c}")
