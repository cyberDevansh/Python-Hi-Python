class calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"THe square is {self.n*self.n}")
    def cube(self):
        print(f"THe cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"THe squareroot is {self.n**(1/2)}")
        
a=calculator(5)
a.square()
a.cube()
a.squareroot()
