#TUPLE
#The tuple is similar to list, BUT
#Can not add, remove, modify the elememts in list

t = (1, 2, 3)
#t[0] = 9 can't use
print(t)

#If you want to modify a tuple
#you can convert it to list and then back into a tuple

l = list(t)
l.insert(2, 10)
t = tuple(l)
print(t)


