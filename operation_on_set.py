set1={'deeksh','pandu','akna',"reddy"}
set2={'sath','wik','reddy'}
set3={'reddy','raghu'}
#print(set1.union(set2))
#print(set2.union(set1))
#print(set1|set2)#  | means union
#set1.update(set2)
#print(set1)
#print(set1.intersection(set2,set3))
print(set1&set2)  # &means intersection
i=set1.intersection(set2,set3)
print(i)