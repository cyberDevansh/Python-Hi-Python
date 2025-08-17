name=input("Enter your name:")
age=int(input("Enter your age:"))
if(age>=18):
    print(f"{name} you are mature now.")
elif(age<0):
    print("Your input is invalid.")
else:
    print("{} you are under age." .format(name))
