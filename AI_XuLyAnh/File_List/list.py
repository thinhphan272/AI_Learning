#Example1
"""
a = 1
string = 'I love Python'
#string[0] = "I"

list = [1, 2, 3, 4, 5, 6, 7]
#Trong đó list[0] = 1
"""

#Example2
"""
#List before
list = [1, 2, 3, 4, 5, 6, 7]
print(f'First element in list before: {list[0]}')

#List after
list[0] = 9
print(f'First element in list afer: {list[0]}')
"""

#Example3
#Check element  in list
list = [1, 2, 3, 4]

print(6 in list)
#Access into elements in list
print(list[1:4])

#Insert the element between the list
list.insert(1,9)
# 1 is index, 9 is new element
print(list)

#Insert the element at the back of list
list.append(5)
print(list)

#Insert new list into the list
newlist = [10, 11, 12]

resultlist = list + newlist
print(resultlist)

#Remove the element in list
list.remove(1)
print(list)

#Remove all the element in list
"""
list.clear()
print(list)
"""

"""Second way
list = []
print(list)
"""

#Sort the list increase
list.sort()
print(list)
#Sort the list decrease
list.sort(reverse=True)
print(list)