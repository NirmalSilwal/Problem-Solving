user_name = input('enter your name: ')

while len(user_name) < 3:
    print('please enter at least 3 character! ')
    user_name = input('enter your name: ')
else:
    template = f'Hello {user_name}, How are you?'

print(template)
