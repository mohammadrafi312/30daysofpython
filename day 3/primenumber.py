n =int(input("enter the number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break


n = int(input("Enter the number: "))

if n < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")