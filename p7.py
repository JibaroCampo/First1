import math
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):

       return"C("+ str(self.radius)+")"
##########test
circle1 = Circle(10)
print "Circle radius:", circle1. radius
print "Circle 1:", circle1

