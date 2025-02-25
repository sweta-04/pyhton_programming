
print("Prime number between 1 to 100")

for i in range(2,100):
	flag=1
	for j in range(2,i):
		if(i%j==0):
			flag=0
			break	
	if(flag ==1):
		print(i)
