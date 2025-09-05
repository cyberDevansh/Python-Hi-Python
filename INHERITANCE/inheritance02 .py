class Employee:
    company = "ITC"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):  
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)   # this is nothing  but Employee.__init__(self, name, salary) means calling init from the parent class
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name}, salary is {self.salary}, and he is good with {self.language} language")


a = Employee("Ramesh", 50000)
b = Programmer("Suresh", 70000, "Python")

a.show()
b.show()
b.showLanguage()

print(a.company, b.company)


#remember  super() is built in  function in python.It automatically finds the parent class