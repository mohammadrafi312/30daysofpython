numbers = [10, 50, 20, 80, 40, 80, 30,50,90]
# print(type(numbers))
# numbers = [10, 50, 20, 80, 40, 80, 30]

largest = 0
second = 0
for num in numbers:
    if num>largest:
        second=largest
        largest=num
print(second)
print(largest)