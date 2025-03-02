# Enter name marks and roll no of student and prin the highest scorer

n = int(input("Enter the no of students :"))

d = {}

for i in range(n) :
	x = {}
	x["name"] = input("Enter the name ")
	x["roll no"] = int(input("Enter roll no "))
	x["Marks"] = int(input("Enter the marks "))
	
	d[i] = x
	
mark_list = []
for i in d:
	mark_list.append(d[i]["Marks"])
	
highest = mark_list.index(max(mark_list))

print("Highest marks :" ,d[highest]["Marks"] , "scored by : " ,d[highest]["name"])
