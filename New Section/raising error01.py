def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero! ARe yrr 0 se kye divide kr rhe ")
    return a / b

print(divide(10, 2))  
print(divide(5, 0))   
