class employee:
    company="ITC"
    
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
    


class Programmer(employee):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=employee()
b=Programmer()

print(a.company, b.company)