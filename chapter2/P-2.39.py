# Develop an inheritance hierarchy based upon a Polygon class that has
# abstract methods area( ) and perimeter( ). Implement classes Triangle,
# Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
# class, with the obvious meanings for the area( ) and perimeter( ) methods.
# Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle,
# and Square, that have the appropriate inheritance relationships. Finally,
# write a simple program that allows users to create polygons of the
# various types and input their geometric dimensions, and the program then
# outputs their area and perimeter. For extra effort, allow users to input
# polygons by specifying their vertex coordinates and be able to test if two
# such polygons are similar.

# im tired

from abc import abstractmethod
from math import sqrt
from math import cos
class Polygon:

    def __init__(self, *args):
        self.p = args

    def area(self):
        # http://www.mathopenref.com/coordpolygonarea2.html
        area = 0
        p = self.p
        j = len(p) - 1
        for i in range(len(self.p)):
            area += (p[j][0] + p[i][0]) * \
                    (p[j][1] - p[i][1])
            j = i
        return abs(area/2)

    def _heron(self, a, b, c):
        s = (a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))


# class Triangle(Polygon):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return self.base * self.height / 2
#
# class Quadrilateral(Polygon):
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def area(self):
#         a,b,c,d = self.a, self.b, self.c, self.d
#         s = (a+b+c+d)/2
#         return sqrt((s-a)*(s-b)*(s-c)*(s-d)-a*b*c*d*cos((A+B)/2)**2)

if __name__ == '__main__':

    xPts = [4, 4, 8, 8, -4, -4];

    yPts = [6, -4, -4, -8, -8, 6];
    points = list(zip(xPts, yPts))
    print(points)
    x = Polygon(*points)
    print(x.area())
    x = Polygon((4,0), (4,4), (0, 4), (0,0))
    print(x.area())
