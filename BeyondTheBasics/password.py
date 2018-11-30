name = input('Enter your name: ')
surname = input('Enter surname: ')
correctPassword = input('Choose a password: ')

password = input('Reenter your password: ')

while correctPassword != password:
    password = input('Incorrect. Please try again: ')

message = 'Hi, %s %s. You have been successfully logged in!' % (name, surname)

print(message)