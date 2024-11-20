
def search(list , element):
    mid=0
    start=0
    end=len(list)
    steps=0

    while(start<=end):
        print('steps',)

    steps=steps+1
    mid=(start + end)//2
    if element ==list[mid]:
        return mid
    if element <list[mid]:
        end =mid-1
        