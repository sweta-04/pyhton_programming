import math
a,b,c=map(float,input("Enter three sides of a triangle : ").split(' '))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("area of triangle is :", area)
