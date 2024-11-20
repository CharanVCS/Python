mydict={
    "key": "value",
    "name":"python",
    "version": "3.10.0",
    "list":[ 1, 2, 3]
}

for a,b in mydict.items():
    print(a,":",b)

def temp(a):
    key = input(f"which value do you want to {mytuple[a]}:")
    value = input(f"what value to want to {mytuple[a]}:")
    mydict[key]=value

mytuple=("change", "update", "add")
while 1:
    choice = int(input("Do you want to change(0) or update(1) or add(2) anything:"))
    temp(choice)
    for a,b in mydict.items():
        print(a,":",b)
