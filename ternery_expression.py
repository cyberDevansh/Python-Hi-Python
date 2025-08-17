age = int(input("Enter your age:"))   #int is used in the starting of the input because input always returns string value even if user entered the integer so we have to typecast the value to the string to compare it with the integer number otherwise the integer and string is not comparable.
status = "Adult" if age >= 18 else "Minor"
print(status)  
