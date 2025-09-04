class Employee:
    def __init__(self, name, salary): # _init_ automatically calls function 
        self.name = name
        self.salary = salary

    def getinfo(self):                
        print(f"{self.name} earns {self.salary}")


p = Employee("Ram", 5000)                          #object p now have= {"name": "Ram", "salary": 5000} we can check by print(p.__dict__)
# print(p.__dict__)
q = Employee("Shyam", 7000)
# print(q.__dict__)

p.getinfo()  
q.getinfo() 

Employee.getinfo(p)
Employee.getinfo(q)
