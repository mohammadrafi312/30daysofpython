# Q5 — Two Sum
# numbers = [2, 7, 11, 15]
# target = 9

# Find the indices of two numbers whose sum equals target.

# Expected:

# [0, 1]

# Try using nested loops first. Don't use a dictionary yet—we'll learn the optimized approach later.

numbers = [2, 7, 11, 15]
target = 9
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            print( i , j)
            
    