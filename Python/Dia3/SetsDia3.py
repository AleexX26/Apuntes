miSet = set([1, 2, 3, 4, 5])
print(type(miSet))
print(miSet)

otro_set = {6, 7, 8, 9, 10}
print(type(otro_set))
print(otro_set)

miSet.add(6)
print(miSet)

miSet.update([11, 12, 13])
print(miSet)

miSet.remove(6)
print(miSet)

otro_set = set([1, 2, 3, 4, 5,(1, 2, 3, 4, 5)])
print(otro_set)
print(len(otro_set))
print(1 in otro_set)

s1 ={1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.union(s2)
print(s3)
