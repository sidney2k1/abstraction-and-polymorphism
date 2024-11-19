class ferrari():
    def fueltype(self):
        print("petrol")
    def maxspeed(self):
        print("Maxspeed is 200")
class bmw():
    def fueltype(self):
        print("Deisel")
    def maxspeed(self):
        print("the maxspeed is 175")
objferrari=ferrari()
objbmw=bmw()
for car in (objferrari,objbmw):
    car.fueltype()
    car.maxspeed()