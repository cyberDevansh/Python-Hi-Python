class Employee:
    @staticmethod
    def greet():
        print("Good Morning")

Employee.greet()



# No self, no cls.
# Declared using @staticmethod.
# Does not depend on object or class data → behaves like a normal function,

# Normal (instance) method = object functions.

# Class method = class-level functions.

# Static method = utility functions inside class.