import math

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

    def top_right_hex_center(self):
        a,b = (self.c.x + (math.sqrt(3)*self.s)/2,self.c.y+self.s*1.5)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)

    def bottom_right_hex_center(self):
        a,b = (self.c.x + (math.sqrt(3)*self.s)/2,self.c.y-self.s*1.5)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)
    
    def bottom_left_hex_center(self):
        a,b=(self.c.x - (math.sqrt(3)*self.s)/2,self.c.y-self.s*1.5)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)

    def top_left_hex_center(self):
        a,b=(self.c.x - (math.sqrt(3)*self.s)/2,self.c.y+self.s*1.5)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)

    def right_hex_center(self):
        a,b=(self.c.x + (math.sqrt(3)*self.s),self.c.y)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)

    def left_hex_center(self):
        a,b=(self.c.x - (math.sqrt(3)*self.s),self.c.y)
        if self.type == 'pointy':
            return Point(a,b)
        elif self.type == 'flat':
            return Point(b,a)
    
    def __str__(self):
        return 'Hexagon({c},{p})'.format(c=self.c,p=self.points())


