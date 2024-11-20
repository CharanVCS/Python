#Printing a tablelist in a file
num =int(input('Enter a number:'))

multiplelist=[i*num for i in range(1,11)]
print(multiplelist)

with open('table.txt','w') as t:
    t.write(f'{multiplelist}\n')