l1 = [1,2,3,4,5,6,7,8,9,47,14,18,25,33,15,54,22]
print(l1)

even = lambda n : n%2==0
l2=filter(even, l1) # fliter works as returns element that true to condition
print(f'even list:{list(l2)}')

odd= lambda n : n%2!=0
l3=filter(odd, l1)
print(f'odd list:{list(l3)}')
