class Employee:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Employee Name: {self.name}")


class Programmer(Employee):      
    def __init__(self, name, language):
        super().__init__(name)   
        self.language = language

    def show_language(self):
        print(f"{self.name} knows {self.language}")


class Manager(Programmer):      
    def __init__(self, name, language, team_size):
        super().__init__(name, language)  
        self.team_size = team_size

    def show_team(self):
        print(f"{self.name} manages a team of {self.team_size} people")



e = Employee("Ramesh")
p = Programmer("Suresh", "Python")
m = Manager("Anita", "Java", 5)


e.show_info()
print("---")
p.show_info()       
p.show_language()
print("---")
m.show_info()        
m.show_language()    
m.show_team()       
