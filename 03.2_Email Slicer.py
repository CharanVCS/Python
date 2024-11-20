# Prompt the user to enter an email address
email = input('Enter your email address? :')

# Slice the email address to extract the username (from the start to the '@' symbol)
user = email[:email.index('@')]

# Slice the email address to extract the domain name (from the '@' symbol to the end)
domain = email[email.index('@') + 1:]

# Construct the output string using the extracted username and domain name
output = 'Your username is {} and your domain name is {}'.format(user, domain)

# Print the output
print(output)

# Prompt the user to press Enter to exit
a = input('Press Enter to exit')
