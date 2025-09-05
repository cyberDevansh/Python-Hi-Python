from random import randint

class Train:
    def book(self, trainno, startingfrom, to):
        print(f"Your train is booked in train number {trainno} from {startingfrom} to {to}")

    def getstatus(self, trainno):
        print(f"Train {trainno} is running on time.")

    def getFare(self, trainno):
        print(f"Your train fare for train {trainno} is {randint(1000,20000)}")

t = Train()
t.book(1234, "Kashmiri Gate", "Orai")
t.getstatus(1234)
t.getFare(1234)
