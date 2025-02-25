import math

x1,y1=map(int,input("Enter coordinates of point 1: ").split(' '))
x2,y2=map(int,input("Enter coordinates of point 2 : ").split(' '))

dist = math.sqrt( pow( (x2-x1),2 )+(pow ( (y2-y1),2 ) ) )

print("Distanc of two points is :", dist)
