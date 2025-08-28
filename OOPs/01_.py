class Employee:
    language="python"
    salary=1000

p = Employee()   # creates a new instance of Employee; changes to p affect only this p object, not the class Employee itself
print(p.salary)

q=Employee  ## q now refers to the class itself, not an object q and any changes will do change inthe employee
print(q.salary)  

q.salary=200
print(Employee.salary,q.salary, p.salary)    #If you don’t assign to p.salary, Python will keep looking at the class so p.salary here giving 200.

p.salary=500
print(Employee.salary,p.salary,q.salary) # si if we change in  object then it will not point to the class