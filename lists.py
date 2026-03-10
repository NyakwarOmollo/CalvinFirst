# 1. Print all values in the list one by one
print("1. Print each value one by one:")
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

print("-" * 40)

# 2. Print each value multiplied by 20
print("2. Each value × 20:")
for num in numbers:
    print(num * 20)

print("-" * 40)

# 3. First letter of each name
print("3. First letter of each name:")
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)           

print("-" * 40)

# 4. Even numbers only
print("4. Even values only:")
all_numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in all_numbers if n % 2 == 0]
print(evens)                   # [2, 4, 6]

print("-" * 40)

# 5. Values present in both lists (intersection)
print("5. Common values in both lists:")
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common = [x for x in list_a if x in list_b]
print(common)                  # [3, 4]

# Alternative using set intersection (more efficient):
# common = list(set(list_a) & set(list_b))

print("-" * 40)

# 6. Reverse each word and make lowercase
print("6. Reversed and lowercase:")
words = ["Elie", "Tim", "Matt"]
reversed_lower = [word[::-1].lower() for word in words]
print(reversed_lower)          # ['eile', 'mit', 'ttam']

print("-" * 40)

# 7. Common letters in two strings (unique & sorted)
print("7. Common letters in 'first' and 'third':")
s1 = "first"
s2 = "third"
common_letters = sorted(set(s1) & set(s2))
print(common_letters)          # ['i', 'r', 't']

print("-" * 40)

# 8. Numbers 1–100 divisible by 12
print("8. Numbers 1–100 divisible by 12:")
div_by_12 = [i for i in range(1, 101) if i % 12 == 0]
print(div_by_12)               # [12, 24, 36, 48, 60, 72, 84, 96]

print("-" * 40)

# 9. Remove vowels from "amazing"
print("9. 'amazing' without vowels:")
word = "amazing"
vowels = "aeiouAEIOU"
no_vowels = [char for char in word if char not in vowels]
print(no_vowels)               # ['m', 'z', 'n', 'g']

print("-" * 40)

# 10. List of lists: [[0,1,2], [0,1,2], [0,1,2]]
print("10. [[0,1,2]] repeated 3 times:")
small_list = [0, 1, 2]
matrix_3x3 = [small_list[:] for _ in range(3)]   # [:] creates copy
print(matrix_3x3)

print("-" * 40)

# 11. 10×10 grid [[0..9], [0..9], ..., [0..9]]
print("11. 10×10 grid (0 to 9 in each row):")
row = list(range(10))               # [0,1,2,3,4,5,6,7,8,9]
grid = [row[:] for _ in range(10)]  # create 10 independent copies
print(grid)