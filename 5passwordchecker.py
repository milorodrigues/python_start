username = input('Enter username ')
password = input('Enter password ')

print(f'{username}\'s password', ('*' * len(password)), f'is {len(password)} characters long.', sep=' ')