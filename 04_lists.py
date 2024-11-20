# list can call values in the form of indexs 
a = 1 ; b ="string" ; c = False

mylist=[a,b,c]
print(mylist)
print(type(mylist))

l1=[ 3, 4, 1]
print(l1[0])
print(l1[1])
print(l1[2])

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(5) # this function add 5 at end of the list 
print(l1)

l1.insert(1,2) # this insert 2 at index 1
print(l1)

l1.pop(4) # removes data in index 4
print(l1)

l1.remove(2) # removes 2 element in the list
print(l1)

l1.insert(0,1)
print(l1)

ct=l1.count(1) # Counts the number of occurrences of an element 1.
print(ct)

l1.pop(3)
print(l1)

l1.extend([2,5])
print(l1)
