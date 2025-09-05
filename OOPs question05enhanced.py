# import random
from random import randint

class train:
    def __init__(self, trainno):
        self.trainno=trainno

    def book(self,startingfrom,to):
        print(f"Your train is booked in train number {self.trainno} from {startingfrom } to {to}")

    def getstatus(self):
        print("Train is running on time.")
    
    def getFare(self):
        print(f"Your train fare is {randint(100,10000)}")


t=train(1234)
t.book("delhi", "orai") 
t.getstatus()
t.getFare()
