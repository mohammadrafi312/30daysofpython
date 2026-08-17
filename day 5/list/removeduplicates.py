# Q3 — Remove Duplicates

# Given:

# numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# Create:

# [1, 2, 3, 4, 5]

# Important: Preserve the original order.
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
result =[]
# print(type(result))
for num in numbers:
    # print(num)
    if num not in result:
        result.append(num)
print(result)