# Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.
import math
class two_D:
    def __init__(self,x,y):
        self.x =x
        self.y =y

    def mag(self):
        return (self.x**2 + self.y**2)**0.5
    def distance(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
    def dot(self,other):
        return (self.x*other.x + self.y*other.y)
    def cross(self,other):
        return self.x*other.y - self.y*other.x
    def rotate(self,theta):
        return two_D(self.x*math.cos(theta)-self.y*math.sin(theta),self.x*math.sin(theta)+self.y*math.cos(theta))
        
        
class three_D(two_D):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z =z
    
    def mag(self):
        xy_mag = super().mag()
        return math.sqrt(xy_mag**2 + self.z**2)
    
    def dot(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self,other):
        x_new = self.y * other.z - self.z * other.y
        y_new = self.z * other.x - self.x * other.z
        z_new = self.x * other.y - self.y * other.x
        return three_D(x_new, y_new, z_new)
        
    


    
        

    

