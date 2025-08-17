n = int(input("Checking whether a number is prime or not\nEnter a number: "))

if n <= 1:
    print("Number is not prime.")
elif n == 2:
    print("Number is prime.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime.")
            break
    else:
        print("Number is prime.")
