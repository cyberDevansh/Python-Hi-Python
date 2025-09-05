# class Employee:
#     a=1

#     def show(self):
#         print(f"The class attribute of a is {self.a}")


    
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    

e= Employee()
e.a =45
e.show()


# just comment this below and remove the first one from teh comment to see how @classmethod and the first one instance method works 