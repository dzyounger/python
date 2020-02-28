#Dai Zhaoyang
#22C:016:A06
#ID: 00719596

import math
class point():

    # This is the initializing method or constructor for the class.
    # Most classes will have one or more constructor methods.
    # Examples: p = point(5, 7) will call this method to construct
    # an instance p of the point class.
    def __init__(self, a, b):
        self.x = a
        self.y = b

    # This translates the point horizontally by a units.
    # This is called as: p.translateX(20)
    def translateX(self, a):
        self.x = self.x + a

    # This translates the point vertically by a units.
    # This is called as: p.translateY(-10)
    def translateY(self, a):
        self.y = self.y + a

    # This returns the Euclidean distance between current point 
    # and the point given as an argument.
    # This is called as: p.distance(point(10, 15))
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
class line(point):

    # The constructor for the line class; constructs the line segment defined by the
    # two given points p1 and p2
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
  
    # Returns the Euclidean length of the line segment
    def length(self):
        return (self.point1).distance(self.point2)

    # Returns the slope of the line segment
    def slope(self):
        if self.point1.x == self.point2.x:
            return None

        return (self.point1.y  - self.point2.y)/(self.point1.x - self.point2.x)

    # Returns a str the represents a line segment. This function is called whenever a string representation of
    # the object is needed
    def __repr__(self):
        return "("+str(self.point1.x) + ", " + str(self.point1.y) + ")---(" + str(self.point2.x) + ", " + str(self.point2.y) + ")"
    
    def intersection(self,L2):
        slope1=self.slope()
        slope2=L2.slope()
        P1x=self.point1.x
        P1y=self.point1.y
        P2x=L2.point1.x
        P2y=L2.point1.y
        a=P1y-P1x*slope1
        b=P2y-P2x*slope2 
        if slope1==slope2:                   #check if two lines arre collinear and intersect
            if a==b:
                return "they are collinear"
            else:
                return "parallell"
        else:
            X1=(b-a)/(slope1-slope2)
            Y1=slope1*X1+a
            return point(X1,Y1)
#main program
L1=line(point(1,3),point(2,5))
L2=line(point(1,2),point(2,3))
print (L1.intersection(L2))
print (L1)