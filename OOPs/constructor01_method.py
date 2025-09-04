class Employee:
    language = "python"
    salary = 1000

    def getinfo(self):  
        print(f"Language is {self.language}. Salary is {self.salary}")
    
    def __init__(self):
        print("I am creating a object which is called automatically (pythons dunder method)")

    @staticmethod
    def greet():
        print("Good Morning.")
p=Employee() #Whenever we create an object, Python automatically calls the __init__ method (constructor) so init method is printed first then other

p.getinfo()
p.greet()