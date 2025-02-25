def hcf(x,y):
	while(y!=0):
		r=x%y
		x=y
		y=r
	return x

def lcm(x,y):
	rem=(x*y)/hcf(x,y)
	return rem
	
x,y=map(int,input("Enter any two number :").split(' '))

print("GCD of two numbers is ",hcf(x,y))
print("Lcm of two numbers is ",lcm(x,y))

