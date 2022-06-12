import math

import matplotlib.pyplot as plt
import numpy as np

# Point Class
class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __str__(self):
        return 'Point({self.x},{self.y})'.format(self=self)

# Hexagon Class
# This class is used to create a hexagon
# The hexagon is created by creating a list of points
class Hexagon:
    # Constructor
    # Input: center Point(x,y), size, type of hexagon (pointy or flat)
    def __init__(self,center,size,type='pointy'):
        if type != 'pointy' and type != 'flat':
            raise Exception("Type values available are 'pointy' and 'flat'")
        self.c,self.s,self.type = center,size,type

    # Calculate one corner of the hexagon
    def corner(self,i):
        deg = 30 if self.type == 'pointy' else 0
        angle_deg = 60 *  i - deg
        angle_rad = math.pi/180 * angle_deg
        return Point(self.c.x + self.s * math.cos(angle_rad), self.c.y + self.s * math.sin(angle_rad))

    # Calculate all the corners of the hexagon
    def points(self):
        x,y=[],[]
        for i in range(1,8):
            x.append(self.corner(i).x)
            y.append(self.corner(i).y)
        return x,y

    def draw_star(self):
        x,y=[self.c.x],[self.c.y]
        for i in range(1,8):
            x.append(self.corner(i).x)
            y.append(self.corner(i).y)
            x.append(self.c.x)
            y.append(self.c.y)
        return x,y

    def top_right_hex_center(self):
        return Point(self.c.x + (math.sqrt(3)*self.s)/2,self.c.y+self.s*1.5)

    def bottom_right_hex_center(self):
        return Point(self.c.x + (math.sqrt(3)*self.s)/2,self.c.y-self.s*1.5)
    
    def bottom_left_hex_center(self):
        return Point(self.c.x - (math.sqrt(3)*self.s)/2,self.c.y-self.s*1.5)

    def top_left_hex_center(self):
        return Point(self.c.x - (math.sqrt(3)*self.s)/2,self.c.y+self.s*1.5)

    def right_hex_center(self):
        return Point(self.c.x + (math.sqrt(3)*self.s),self.c.y)

    def left_hex_center(self):
        return Point(self.c.x - (math.sqrt(3)*self.s),self.c.y)


# Initial center and size of the first hexagon (in the center)
ix,iy,size=1,1,3

# Center Hexagon
p1 = Point(ix,iy)
hex1 = Hexagon(p1,size)
x,y = hex1.points()
plt.plot(x,y,color='blue')

# Top Right Hexagon
p2 = hex1.top_right_hex_center()
hex2 = Hexagon(p2,size)
x2,y2 = hex2.points()
plt.plot(x2,y2,color='red')

# Right Hexagon
p3 = hex1.right_hex_center()
hex3 = Hexagon(p3,size)
x3,y3 = hex3.points()
plt.plot(x3,y3,color='green')

# Bottom Right Hexagon
p4 = hex1.bottom_right_hex_center()
hex4 = Hexagon(p4,size)
x4,y4 = hex4.points()
plt.plot(x4,y4,color='yellow')

# Bottom Left Hexagon
p5 = hex1.bottom_left_hex_center()
hex5 = Hexagon(p5,size)
x5,y5 = hex5.points()
plt.plot(x5,y5,color='orange')

# Left Hexagon
# p6 = Point(ix-(math.sqrt(3)*size),iy)
p6 = hex1.left_hex_center()
hex6 = Hexagon(p6,size)
x6,y6 = hex6.points()
plt.plot(x6,y6,color='purple')

# Top Left Hexagon
p7 = hex1.top_left_hex_center()
hex7 = Hexagon(p7,size)
x7,y7 = hex7.points()
plt.plot(x7,y7,color='black')


plt.show()
