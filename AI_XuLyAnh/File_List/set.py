#SET use "{ }"
#The data in a set has no order
#Cannot change, don't accept duplicate values
#While create a set if have duplicate values a set will skip
#just take only one values

#Elements in the set can have any data type
#and can have more than 1 data type in a set

#Operation with set
set1 = {1, 2, 3}
set2 = {2, 9}
#Loop through the elements in set
for i in set1:
    print(i)

#Check the element in set
print(7 in set1)

#Add the element into set
set1.add(5)
print(set1)

#Add values in other set with update/union
newset = set1.union(set2)
print(newset)

#Remove values in set with remove/discard
newset.discard(2)
print(newset)

#Remove all values in set with clear
newset.clear()
print(newset)