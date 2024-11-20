films = {
    'RRR':[6, 80],
    'Avatar':[10, 100],
    'The_Wolf_Of_Wall_Street':[18, 50],
    'After':[18, 50]
}

choice = input('Which film you would like to watch? :').strip().title()
if choice in films :
    age = input('How old are you?:').strip()
    if int(age) >= films[choice][0]:
        if films[choice][1]>0:
            print("Enjoy the film")
            films[choice][1] = films[choice][1] -1
        else :
            print('sorry!,seats are sold')
    else:
        print("You are too young to see that film")
else:
    print("we don't have that film..") 