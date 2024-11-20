f =open('filepy.txt','w') #open file in 'w'rite mode
f.write('This file created by python code\n')
f.write('also second line')
f.close()

f =open('filepy.txt','r') #open file in 'r'ead mode
text =f.read()
# text =f.readlines() #it reads file as list[]
print(text)
f.close()

# f =open('filepy.txt','a') #open file in 'a'ppend mode
# f.write('\nthird line')
# f.close()

#another way to open files
#'with' statement it automatically open and close files

# with open('filepy.txt') as f:
#     text=f.read()
#     print(text)
