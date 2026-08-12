num =int(input("enter the number:"))


if num > 0 and num%2==0:
    print("positive even")

elif num > 0 and num%2 != 0:
    print("positive odd")

elif num <0 and num%2==0:
    print("negative even")

elif  num < 0 and num%2 != 0:
    print("negative  odd")
else: 
    print("zero")