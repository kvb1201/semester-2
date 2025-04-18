# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
# yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
# should be a method that returns the length converted into those units. For example, using the
# Converter object created above, the user could call c.feet() and should get 0.75 as the result.

class Converter:
    def __init__(self,length,unit):
        self.length = length
        self.unit = unit
    def simplifier(self):
        if(self.unit == "m"):
            self.length /=100
        elif(self.unit == "km"):
            self.length /=1000
        elif(self.unit == "mm"):
            self.length *= 10
        elif(self.unit == "inch"):
            self.length *=2.5
        elif(self.unit == "feet"):
            self.length /= 30
        elif(self.unit == "cm"):
            self.length *=1
        else:
            print("Invalid unit")
    def cm(self):
        self.simplifier()
        return self.length
    def m(self):
        self.simplifier()
        self.length /= 10
        return self.length
    def km(self):
        self.simplifier()
        self.length /= 100
        return self.length
    def inch(self):
        self.simplifier()
        self.length /= 2.5
        return self.length
    def feet(self):
        self.simplifier()
        self.length /= 30
        return self.length
    

p1 = Converter(1,"inch")
print(p1.cm())


        