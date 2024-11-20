a = input('File name: ').lower().strip()

if a.endswith(('.gif','.png')):
    print('image/' + a.rsplit('.', 1)[1])
elif a.endswith(('.jpg', '.jpeg')):
    print('image/jpeg')
elif a.endswith(('.pdf', '.zip')):
    print('application/'+a.rsplit('.', 1)[1])
elif a.endswith('.txt'):
    print('text/plain')
else:
    print('application/octet-stream')
