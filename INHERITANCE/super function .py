class Employee():
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c=3

class Users(Manager):
    def __init__(self):
        super().__init__()   # this will now run the parent constructor also 
        print("Constructor of Users")
    d=4


print("-----")
o=Employee()
print(o.a)  # only EMployee constructor will run means the init in class employee Only Employee.__init__ executes.
print("-----")

o=Programmer()
print(o.a, o.b)   # only Programmer constructor will run  means the init in class Programmer
print("-----")


o=Manager()
print(o.a,o.b,o.c)   # only Manager constructor will run  means the init in class Manager
print("-----")


o=Users()
print(o.a,o.b,o.c,o.d)   #now the parent constructor will also run due to super function 
print("-----")

