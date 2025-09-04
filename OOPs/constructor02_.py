class Employee:
    language = "python"
    salary = 1000

    def __init__(self, name , salary, language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object.")

    def getinfo(self):  
        print(f"Language is {self.language}. Salary is {self.salary}")
    


    @staticmethod
    def greet():
        print("Good Morning.")

p=Employee("Devansh", 2004 , "Javascript")
print(p.name,p.salary, p.language)
