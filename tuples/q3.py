# writea user defined function to find comon elemnts among three lists

def common(x,y,z):
	set1 = set(x)
	set2 = set(y)
	set3 = set(z)
	
	a = list(set1 & set2 & set3)
	print("Common elemts from three list are ", a)

print("Enter the elemts of list 1 ")
x = map(int,input().split(' '))

print("Enter the elemts of list 2 ")
y = map(int,input().split(' '))

print("Enter the elemts of list 3 ")
z = map(int,input().split(' '))

common(x,y,z)
