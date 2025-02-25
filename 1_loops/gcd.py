
a,b=map(int,input("Enter two numbers to find their GCD :").split(' '))

gcd=1
small=min(a,b)

for i in range(1, small+1):
	if(a%i==0 and b%i==0):
		gcd =i
		
print("Gcd is " , gcd)
