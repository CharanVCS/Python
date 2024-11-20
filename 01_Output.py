v1 = 'World!'
v2 = 1.14

# types of output methods are defined in the standard library.
print('Hello '+ v1) # concatination
print('Hello ', v1)  

print(f'Hello {v1}') # fstring representation 
print('Hello {}'.format(v1)) # by using format() function

# %%
print('Hello %s\nfloat number: %s' % (v1, v2))

#%%
# printing value upto decimal digits
print(f"{v2:.5f}")