#Basic syntax of for_loop
for i in range(11):
    print(i)

# print('even numbers from 0 to 10:')
# for i in range(0,11,2): #2 in the range used to skip 2 times of loop after excute the code
#     print(i)

a =['item1','item2','item3','item4']
for i in range(len(a)):
    print(a[i])
print("\n",end='')
for i in a:
    print(i)
    
