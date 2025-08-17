n=int(input("Enter a number:"))

for i in range (11):
    print(f"{n} * {i} = {n*i} ")

n=int(input("Enter a number:"))

# second method to do that 

for i in range (10):
    i+=1
    print(f"{n} * {i} = {n*i} ")