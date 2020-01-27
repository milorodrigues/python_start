longstring ='''
   O
  //
   |
  //
idk how to escape the backslash
also if you put the 3 quotes in another line it registers that final newline
'''

print(longstring)

longstring2 = '''
i found out how to escape the backslash
  O
  /\\
  |
  /\\'''

print(longstring2)

users_name = "john"
users_age = 55
print(f"hi {users_name}. you are {users_age} years old.")

string1 = "hi {}. you are {} years old."
print(string1.format(users_name, users_age))

string2 = "you are {1} years old, {0} from {2}."
print(string2.format(users_name, users_age, 'australia'))

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

numbers = '0123456789'
print(numbers[4])
print(numbers[2:6])
print(numbers[5:])
print(numbers[:3])
print(numbers[1:8:2])
print(numbers[::3])

print(numbers[-2])
print(numbers[2:-4])
print(numbers[::-1])
print(numbers[::-2])