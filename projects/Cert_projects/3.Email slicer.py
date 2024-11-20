email = input('Enter your email address? :')
user = email[:email.index('@')].capitalize()
domain=email[email.index('@')+1:]
output ='your username is {} and your domain name is {}'.format(user,domain)
print(output)
end=input('press Enter to exit')