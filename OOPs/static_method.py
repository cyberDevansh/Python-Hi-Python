class Employee:
    language = "python"
    salary = 1000

    def getinfo(self):  
        print(f"Language is {self.language}. Salary is {self.salary}")

    # def greet(self):  
    #     print("Good Morning.")
    # ↑ This would work, but since greet() doesn’t use self or any instance variables,
    #   we don’t really need to make it a regular method.

    @staticmethod
    def greet():
        print("Good Morning.")
p=Employee()

p.getinfo()
p.greet()

# A normal method (like getinfo) takes 'self' because it needs access to the object (its data: language, salary, etc.).
# But 'greet' does not use any object data, so we can make it a @staticmethod.
# A static method does not take 'self' and can be called on the class or object.
