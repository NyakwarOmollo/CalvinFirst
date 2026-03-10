# 1. Largest Number (fixed)
def largest_number(a, b, c):
    """
    Returns the largest of three numbers.
    """
    return max(a, b, c)


# Test
print("Largest number:", largest_number(8, 9, 7))      # → 9
print("Largest number:", largest_number(100, 42, 999)) # → 999


# 2. Check for letter in word (already correct – just improved style)
def check_letter_in_word(letter, word):
    """
    Returns True if the letter is found in the word, False otherwise.
    Case-sensitive.
    """
    return letter in word


# Tests
print("Is 'a' in 'apple'?", check_letter_in_word("a", "apple"))   # True
print("Is 'b' in 'apple'?", check_letter_in_word("b", "apple"))   # False
print("Is 'A' in 'apple'?", check_letter_in_word("A", "apple"))   # False


# 3. Count to a number (already correct – just added header)
def count_to_number(n):
    """
    Prints numbers from 1 to n inclusive.
    """
    print(f"Counting from 1 to {n}:")
    for i in range(1, n + 1):
        print(i)


# Test
count_to_number(5)