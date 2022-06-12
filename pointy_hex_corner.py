import math
import numpy as np
import matplotlib.pyplot as plt

# Point Class
class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __str__(self):
        return 'Point({self.x},{self.y})'.format(self=self)

# Hexagon Class
class Hexagon:
    # Constructor
    # Input: center, size, type of hexagon (pointy or flat)
    def __init__(self,center,size,type='pointy'):
        if type != 'pointy' and type != 'flat':
            raise Exception("Type values available are 'pointy' and 'flat'")
        self.c,self.s,self.type = center,size,type

    # Calculate the corner of the hexagon
    def corner(self,i):
        deg = 30 if self.type == 'pointy' else 0
        angle_deg = 60 *  i - deg
        angle_rad = math.pi/180 * angle_deg
        return Point(self.c.x + self.s * math.cos(angle_rad), self.c.y + self.s * math.sin(angle_rad))

    # Calculate all the corners of the hexagon
    def draw_out(self):
        x,y=[],[]
        for i in range(1,8):
            x.append(self.corner(i).x)
            y.append(self.corner(i).y)
        return x,y

    def draw_in(self):
        x,y=[self.c.x],[self.c.y]
        for i in range(1,8):
            x.append(self.corner(i).x)
            y.append(self.corner(i).y)
            x.append(self.c.x)
            y.append(self.c.y)
        return x,y

ix,iy,size=1,1,3

# Center Hexagon
p1 = Point(ix,iy)
hex1 = Hexagon(p1,size)
x,y = hex1.draw_out()
plt.plot(x,y,color='blue')

# Top Right Hexagon
p2 = Point(ix+(math.sqrt(3)*size)/2,iy+size*1.5)
hex2 = Hexagon(p2,size)
x2,y2 = hex2.draw_out()
plt.plot(x2,y2,color='red')

# Right Hexagon
p3 = Point(ix+(math.sqrt(3)*size),iy)
hex3 = Hexagon(p3,size)
x3,y3 = hex3.draw_out()
plt.plot(x3,y3,color='green')

# Bottom Right Hexagon
p4 = Point(ix+(math.sqrt(3)*size)/2,iy-size*1.5)
hex4 = Hexagon(p4,size)
x4,y4 = hex4.draw_out()
plt.plot(x4,y4,color='yellow')

# Bottom Left Hexagon
p5 = Point(ix-(math.sqrt(3)*size)/2,iy-size*1.5)
hex5 = Hexagon(p5,size)
x5,y5 = hex5.draw_out()
plt.plot(x5,y5,color='orange')

# Left Hexagon
p6 = Point(ix-(math.sqrt(3)*size),iy)
hex6 = Hexagon(p6,size)
x6,y6 = hex6.draw_out()
plt.plot(x6,y6,color='purple')

# Top Left Hexagon
p7 = Point(ix-(math.sqrt(3)*size)/2,iy+size*1.5)
hex7 = Hexagon(p7,size)
x7,y7 = hex7.draw_out()
plt.plot(x7,y7,color='black')


plt.show()
