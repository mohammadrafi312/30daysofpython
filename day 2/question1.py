# Convert this into a single conditional expression:

# age = 20

# if age >= 18:
#     result = "Eligible"
# else:
#     result = "Not Eligible"
age =int(input("enter age:"))
result = "Eligible" if age >=18 else "Not Eligible"
print(result)