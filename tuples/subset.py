#program to get all subsets of a given size of sets
import itertools as it
a = {23, 12, 44,95}

x = int(input("Enter teh size of subset"))
b = set(it.combinations(a,x))
print(b)
