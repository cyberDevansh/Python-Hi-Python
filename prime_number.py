# printing numbers between input digit starting from zero
n=int(input("Printing prime numbers from zero:\nEnter a number:"))
if n<=1:
    print("No a prime number exist in between. Maybe invalid input.")
else:
    for i in range(2,n):
        if n%i==0:
            continue
        elif n==2:
            print(n)
            continue
        else:
            print(i)
            continue

            # /// wrong code still needs to be coreected
        """
        dihfoa
        """