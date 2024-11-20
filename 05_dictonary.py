# dictonary can calls value in the form of text

mydict={
    "key": "value",
    "name":"pyhton",
    "version": "3.10.0",
    "list":[ 1, 2, 3]
}

print(mydict)

print(mydict["name"])
print(mydict["version"])
print(mydict["list"])

#mydict.update({}) used to add or replace data
mydict.update({"version":"3.12.0"})
print(mydict)

# Other way to add data
mydict["OOPS"] = "YES"
print(mydict)

# print(mydict.get('list2')) #mydict.get('') used to print value of that key in dictonary 
# print(mydict.get('list'))

# for a,b in mydict.items(): #mydict.item() used to print both keys and values
#     print(a,":",b)

# for a in mydict.keys(): #mydict.keys() used to print only keys
#     print(a)
