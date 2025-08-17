name="dev"
def greet():
    print("Good Day, "+ name)
    return "hello"
a=greet()   #  this will store the return of the function not the function 
print(a)

b=greet        #this will store the function code and not the return value 
print(b)  # this will not print or run the function it is maybe pointer of the b or greet
b()      # this will actrually print the function in b which is greet but it wil not show the return value 

print(greet())    #this will show the greet as well as retrun value