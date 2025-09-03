class Employee:
    language="python"
    salary=1000
    def getinfo(itis):
        print(f"Language is {itis.language}. Salary is {itis.salary}") # so now i found that there is no need to give self instead we can give any name

p = Employee()   
p.language="Javascript"
print(p.language)

p.getinfo() #python read this as Employee.getinfo(p)
