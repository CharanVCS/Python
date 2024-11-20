def process ( list, word):
    word = word.strip() #strip() func is used to remove spaces in the string
    word = word.lower()
    if word in list:
     list.remove(word)
    return list

list=['python','java','javascript','clang','html']

l1=process(list,'  java  ')
print(l1)
