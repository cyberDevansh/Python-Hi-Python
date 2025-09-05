class Programmer:
    company="Microsoft"

    def __init__(self, name, pincode, salary):
        self.name=name
        self.pincode=pincode
        self.salary=salary


a=Programmer("Devansh", 285001,2000000 )
print(f"Name={a.name}\nPincode={a.pincode}\nCompany={ a.company}\nSalary={ a.salary}")  
b=Programmer("Ansh", 285801,2000400 )
print(f"\tName={b.name}\tPincode={b.pincode}\tCompany={ b.company}\tSalary={ b.salary}")  
