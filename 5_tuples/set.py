set1 = {20,30,12,45}
set2 = {2,54,12,30}

print(set1)
print(set2)

print("Intersection is ", set1 & set2)
print("Union is ", set1 |set2)
print("Differnnce is ", set1-set2)

# do using functions

print("Intersection is ", set1.intersection(set2))
print("Union is ", set1.union(set2))
print("Differnnce is ", set1.difference(set2))
