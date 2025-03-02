try :
	a,b = map(int,input("Enter the numbers ").split(' '))
	print(a/b)

except ZeroDivisionError :
	print("Error in divsion ")
	
except ValueError as ve:
	print(ve)
