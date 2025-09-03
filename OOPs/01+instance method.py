class Employee:
    def getinfo(self): #instance method
        print(f'Language is {self.language}. Salary is {self.salary}')

p=Employee()
p.language="python"
p.salary=5000
p.getinfo()



#First parameter is self, which represents the object (instance).
#Can access and modify object data (self.language, self.salary).