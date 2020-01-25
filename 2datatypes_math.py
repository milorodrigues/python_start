#Data Types

#Fundamental Data Types
int
float

print((2 + 4), end=' ') #end specifies the last character of the string; default is \n
print(type(2 + 4))
print((2 - 4), end=' ')
print(type(2 - 4))
print((2 * 4), end=' ')
print(type(2 * 4))
print((2 / 4), end=' ')
print(type(2 / 4))
print((2 % 4), end=' ')
print(type(2 % 4))
print((2 ** 3), end=' ') #power
print(type(2 ** 3))
print((2 // 4), end=' ') #division, rounding the result to the nearest integer
print(type(2 // 4))
print((5 // 4), end=' ')
print(type(5 // 4))

print() #newline

print((20 + 1.1), end=' ')
print(type(20 + 1.1))
print((9.9 + 2.1), end=' ')
print(type(9.9 + 2.1))

print()
print(bin(5)) #apparently only takes integers as argument
print(int('0b101', 2)) #apparently only takes strings in the first argument
print(int('101', 2))

bool
str
list
tuple
set
dict

#Math functions

print()
print((round(3.1))) #rounds to the nearest int
print((round(3.5))) #.5 rounds up
print((round(3.7)))

print()
print(abs(-23))

#Variables

print()
iq = 190
print(iq, end=' ')
print(type(iq))

iq = float(190)
print(iq, end=' ')
print(type(iq))

a, b, c = 1, 0.5, "hi"
print(a, end=" ")
print(b, end=" ")
print(c)
print(str(a) + " " + str(b) + " " + c)

#Classes

#Specialized Data Types

#Others
None