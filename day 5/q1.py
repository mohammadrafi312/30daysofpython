# 💼 Company-Level Q1 — First Non-Repeating Element

# Given:

# numbers = [4, 5, 1, 2, 1, 5, 4, 7, 2]

# Find the first element that appears exactly once.

# Expected:

# 7
# Requirements
# Use a list/tuple and dictionary or list logic.
# Don't use Counter.
numbers = [4, 5, 1, 2, 1, 5, 4, 7, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in numbers:
    if frequency[num] == 1:
        print(num)
        break