class Employee:
    company="Google"

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company


print(Employee.company)
Employee.change_company("Microsoft")
print(Employee.company)



#First parameter is cls, which represents the class itself
#Declared using @classmethod
#Can access/modify class variables, but not instance variables directly.