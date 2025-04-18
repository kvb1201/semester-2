# Create a base class "Shape" with methods to calculate the area and perimeter. Implement
# derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
# and perimeter calculations.

class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class rectangle(shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
class circle(shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 6.28 *self.radius
    
    def area(self):
        return 3.14 *self.radius*self.radius
        
        