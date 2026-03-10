# 1. Convert list of tuples to dictionary
print("1. Convert list of tuples to dictionary:")
data = [("name", "Elie"), ("job", "Instructor")]

# Method A: Dictionary comprehension (clean & modern)
person = {key: value for key, value in data}
print(person)  # {'name': 'Elie', 'job': 'Instructor'}

# Method B: Using dict() constructor (very common)
person2 = dict(data)
print(person2)  # same result

print("-" * 50)


# 2. Create dictionary from two lists (zip + dict)
print("2. Dictionary from two lists (abbreviations → full names):")
abbrevs = ["CA", "NJ", "RI"]
full_names = ["California", "New Jersey", "Rhode Island"]

states = dict(zip(abbrevs, full_names))
print(states)
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

print("-" * 50)


# 3. Create vowel dictionary with value 0 (without fromkeys)
print("3. Vowels dictionary with value 0 (no fromkeys):")
vowels = 'aeiou'

# Method A: Dictionary comprehension
vowel_dict = {letter: 0 for letter in vowels}
print(vowel_dict)  # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Method B: Manual creation (also fine)
vowel_dict2 = {}
for letter in vowels:
    vowel_dict2[letter] = 0
print(vowel_dict2)  # same result

print("-" * 50)


# 4. Alphabet position → letter dictionary (1:A, 2:B, ..., 26:Z)
print("4. Alphabet position to letter dictionary:")
alphabet_dict = {}

# Using chr() function (ASCII/Unicode)
for i in range(1, 27):
    letter = chr(64 + i)          # 65 = 'A', so 64 + 1 = 'A'
    alphabet_dict[i] = letter

print(alphabet_dict)
# {1: 'A', 2: 'B', ..., 26: 'Z'}

# Alternative one-liner (more compact):
alphabet_dict_comp = {i: chr(64 + i) for i in range(1, 27)}
print(alphabet_dict_comp)  # same result