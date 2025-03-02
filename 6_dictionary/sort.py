# sort the dictionary in ascendign and descending order

dict = {'A' :7, 'B' : 8, 'C' : 1, 'D' : 87}
print("Before sorting" ,dict)

l1 = list(sorted(dict.values()))
print("Ascending order ", l1)

l2 =  list(sorted(dict.values() , reverse = True))
print("Descending order ", l2)
