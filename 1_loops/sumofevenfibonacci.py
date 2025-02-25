
a,b,c,s=0,1,0,0

while(c<4000):
	c=a+b
	print(c, end=" ")
	a=b
	b=c
	if(c%2==0):
		s = s+c
print("sum of even fibonacii numbers is :",s) 
