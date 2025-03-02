# concatenate 3 dictinaries to 1 dictionary

d1 = {'A' : 2, 'B' :4, 'C' : 9}
d2  = {'NAME' : "SWETA", 'DEPT' : "CSE"}
d3 = {'D' : 3, 'E' : 7}

res = {}
for i in (d1,d2,d3):
	res.update(i)
print("Modified dictionary" , res)
	


