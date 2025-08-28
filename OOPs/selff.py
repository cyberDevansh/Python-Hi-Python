class Employee:
    language = "Python"
    salary = 1000

    def getinfo(self):
        print(f"Language is {self.language}, Salary is {self.salary}")

p = Employee()       
q = Employee()      

p.language = "JavaScript"   
q.language = "C++"         

p.getinfo()  
q.getinfo() 
