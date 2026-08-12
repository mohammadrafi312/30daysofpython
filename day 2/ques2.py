num =int(input("enter the number:"))
if num == 0:
    print("zero")

if num > 0 and num%2==0:
    print("positive even")

if num > 0 and num%2 != 0:
    print("positive odd")

if num <0 and num%2==0:
    print("negative even")

if num < 0 and num%2 != 0:
    print("negative  odd")