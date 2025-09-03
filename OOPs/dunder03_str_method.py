class Employee:
    def __str__(self):
        return "This is an Employee object"

e = Employee()
print(e) # Python calls Employee.__str__(e) under the hood. either we can do print(Employee()) so in both condition they are same read

