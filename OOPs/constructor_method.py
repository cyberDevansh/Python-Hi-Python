class Employee:
    language = "python"
    salary = 1000

    def getinfo(self):  
        print(f"Language is {self.language}. Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning.")
p=Employee()

p.getinfo()
p.greet()
