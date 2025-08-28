class Employee:
    def __init__(self, name, salary): # _init_ automatically calls function 
        self.name = name
        self.salary = salary

    def getinfo(self):                
        print(f"{self.name} earns {self.salary}")


p = Employee("Ram", 5000)
q = Employee("Shyam", 7000)

p.getinfo()  
q.getinfo() 

Employee.getinfo(p)
Employee.getinfo(q)
