num = int(input("Enter the number to check Armstrong: "))

count = 0
original = num
temp = num

# Count digits
while temp > 0:
    temp //= 10
    count += 1

# Calculate Armstrong sum
temp = num
sum_of_digit = 0

while temp > 0:
    digit = temp % 10
    sum_of_digit += digit ** count
    temp //= 10

# Check
if original == sum_of_digit:
    print("Armstrong")
else:
    print("Not Armstrong")