username = input()
password = input()
login_password = ''

while login_password != password:
    login_password = input()
print(f'Welcome {username}!')
