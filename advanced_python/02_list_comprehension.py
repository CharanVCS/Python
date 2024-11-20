list1=[5, 4, 3, 2, 1]

for i, e in enumerate(list1):
    print(f'element number {iṇ} is {e}')

# list2=[]
# for i in list1:
#     list2.append(i*i)

list2=[ i*i for i in list1 if i>2] # list comprehension method
print(list2)
