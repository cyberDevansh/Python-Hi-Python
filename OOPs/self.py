class Employee:
    language="python"
    salary=1000
    def getinfo():
        print(f"Language is {language}. Salary is {salary}")

p = Employee()   
p.language="Javascript"
print(p.language)

p.getinfo() #python read this as Employee.getinfo(p)
