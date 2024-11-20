mylist=[2, 4, 6, 8]

square = lambda n: n*n
l1=map(square, mylist) # here map() works as returns results of lambda 
print(list(l1))
