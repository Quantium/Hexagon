import matplotlib.pyplot as plt
from pointy_hex_corner import Point, Hexagon

# Initial center of the first hexagon (in the center), and size and type of all the hexagons
ix,iy,size,t=1,1,3,'pointy'

# Center Hexagon
p1 = Point(ix,iy)
hex1 = Hexagon(p1,size,t)
x,y = hex1.points()
plt.plot(x,y,color='blue')

# Top Right Hexagon
p2 = hex1.top_right_hex_center()
hex2 = Hexagon(p2,size,t)
x2,y2 = hex2.points()
plt.plot(x2,y2,color='red')

# Right Hexagon
p3 = hex1.right_hex_center()
hex3 = Hexagon(p3,size,t)
x3,y3 = hex3.points()
plt.plot(x3,y3,color='green')

# Bottom Right Hexagon
p4 = hex1.bottom_right_hex_center()
hex4 = Hexagon(p4,size,t)
x4,y4 = hex4.points()
plt.plot(x4,y4,color='yellow')

# Bottom Left Hexagon
p5 = hex1.bottom_left_hex_center()
hex5 = Hexagon(p5,size,t)
x5,y5 = hex5.points()
plt.plot(x5,y5,color='orange')

# Left Hexagon
p6 = hex1.left_hex_center()
hex6 = Hexagon(p6,size,t)
x6,y6 = hex6.points()
plt.plot(x6,y6,color='purple')

# Top Left Hexagon
p7 = hex1.top_left_hex_center()
hex7 = Hexagon(p7,size,t)
x7,y7 = hex7.points()
plt.plot(x7,y7,color='black')

plt.show()
