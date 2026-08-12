side1 =int(input("enter side1 :"))
side2 =int(input("enter side2 :"))
side3 =int(input("enter side3 :"))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1 :
    print("valid triangle")
    if side1==side3 and side1 == side2:
         print("equlator triangle")
    elif side1 != side2 and side1!=side3 and side2 != side3:
         print("scalene triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isoscelene")
else :
     print("invalid triangle")


  