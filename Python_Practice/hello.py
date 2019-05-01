#!/usr/bin/python
x = 1
if x == 1:
	print("x is 1")

one = 1
two = 2
hello = ' hello'
print (str(one + two)+ hello)

str = 'Hello Sezan!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

list1 = ['sezan', 'saimon', 1991, 5.0]
list2 = ['shadman', 'sazid']

print list1          # Prints complete list
print list1[0]       # Prints first element of the list
print list1[1:3]     # Prints elements starting from 2nd till 3rd 
print list1[2:]      # Prints elements starting from 3rd element
print list2 * 2  # Prints list two times
print list1 + list2 # Prints concatenated lists

tuple = ('sezan', 'saimon', 1991, 5.0)
tuple1 = ('shadman', 'sazid')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tuple1 * 2   # Prints list two times
print tuple + tuple1 # Prints concatenated lists

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str
print 'C:\\nowhere'

