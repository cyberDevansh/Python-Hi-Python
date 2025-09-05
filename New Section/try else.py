def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:      #Runs only if no error happens in the try means try run then else also run 
        print(" Division successful, result is:", result)

divide(10, 2)  
divide(5, 0)    
