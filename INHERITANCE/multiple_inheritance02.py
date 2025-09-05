class Employee:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Employee Name: {self.name}")


class Coder:
    def __init__(self, language):
        self.language = language

    def show_language(self):
        print(f"Knows programming language: {self.language}")


class Programmer(Employee, Coder):

    def __init__(self, name, language, experience):
        Employee.__init__(self, name)
        Coder.__init__(self, language)
        self.experience = experience


    def show_experience(self):
        print(f"{self.name} has {self.experience} years of experience")


p = Programmer("Suresh", "Python", 5)

p.show_info()      
p.show_language()   
p.show_experience() 
