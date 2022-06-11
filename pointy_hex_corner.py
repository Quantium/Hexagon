import math
import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __str__(self):
        return 'Point({self.x},{self.y})'.format(self=self)

class Hexagon:
    def __init__(self,center,size,type='pointy'):
        if type != 'pointy' and type != 'flat':
            raise Exception("Type values available are 'pointy' and 'flat'")
        self.c,self.s,self.type = center,size,type

    def corner(self,i):
        deg = 30 if self.type == 'pointy' else 0
        angle_deg = 60 *  i - deg
        angle_rad = math.pi/180 * angle_deg
        return Point(self.c.x + self.s * math.cos(angle_rad), self.c.y + self.s * math.sin(angle_rad))

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

p1 = Point(ix,iy)
hex1 = Hexagon(p1,size)
x,y = hex1.draw_out()
plt.plot(x,y)

p2 = Point(ix+(math.sqrt(3)*size)/2,iy+size*1.5)
hex2 = Hexagon(p2,size)
x2,y2 = hex2.draw_out()
plt.plot(x2,y2)

p3 = Point(ix+(math.sqrt(3)*size),iy)
hex3 = Hexagon(p3,size)
x3,y3 = hex3.draw_out()
plt.plot(x3,y3)

p4 = Point(ix+(math.sqrt(3)*size)*1.5,iy+size*1.5)
hex4 = Hexagon(p4,size)
x4,y4 = hex4.draw_out()
plt.plot(x4,y4)

plt.show()
