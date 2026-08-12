num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num2 < num1 < num3) or (num3 < num1 < num2):
    print(f"Middle number: {num1}")

elif (num1 < num2 < num3) or (num3 < num2 < num1):
    print(f"Middle number: {num2}")

else:
    print(f"Middle number: {num3}")