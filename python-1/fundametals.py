# Multi-line construct
from gc import set_debug


the_world_is_flat = True
if the_world_is_flat:
    print("Be careful, not to fall off!")

# This is a comment
spam = 1  # and this is also a comment
# ... and also another!

text = "# This is not a comment, rather a string literal"

print(2 + 2)

print(50 - 5*6)

print((50 - 5*6) / 4)

print(8 / 5)  # Returns a float-type value

# To get a int type in a division, we can use floor-division

print(8 // 5)

# To calculate powers, we can use ** operator.

print(8 ** 5)

width = 20
height = 5 * 9

print(width * height)

# If a variable is not defined trying to use it, will give an error

# print(n)

# Operators with mixed-type operands, convert integer operand to floating point.

print(4 * 3.5 + 1)

# Python has suport for number like Decimal and Fraction, other than int or float, also complex numbers

complex_1 = 3 + 5j

print(complex_1)

# Strings

# Following declarations are possible while declaring strings.

string_1 = 'spam eggs'
string_2 = 'doesn\'t'
string_3 = "doesn't"
string_4 = '"Yes", they said'
string_5 = "\"Yes\", they said"
string_6 = '"Isn\'t", they said'

print("String declarations: %s %s %s %s %s %s" % (string_1, string_2,
      string_3, string_4, string_5, string_6))

# If a character prefaced by '\' shouldn't be treated as special characters, we can use raw strings.

print(r'C:\Users\goura\new')

# It's possible to write multi-line string

# A '\' character at end of empty line is to skip printing an empty line
print("""\ 
Usage: thingy [OPTIONS]
     -h                 Display this usage message
     -H hostname        Hostname to connect to
""")
# Strings can be concatenated with another string and multiplied by an integer value

print(3 * 'um' + 'um')

# Two or more string literals place next to each other are automatically indented

print("Um" "er" "23")

# to work with variables, '+' is needed

seed = "Python"
print("Jy" + seed[2:])

# Strings can be indexed
print(seed[2])

print(seed[4])

# Indexes can also be -ve, whch starts from -1, which is the last character of a string

print(seed[-1])

# Slicing in string is also supported

print(seed[0:2])  # Last index character is not included

# First index, if not present, defaults to zero, for last index, it defaults to length of string.

print(seed[0:])

print(seed[:6])

# Since starting index is always included and ending index is always discarded, so seed[:i] + seed[i:] = entire string

print(seed[:3] + seed[3:])  # Python

# Trying to access a character using invalid index, results in error.

# But in slicing, presence of invalid indexes are handed gracefully

# print(seed[34]) # Error

print(seed[2:45])

# Python stings are immutable, and cannot be changed.

# seed[3] = 'r'

# print(seed)  # error

# For a different string, we can store it in another variable

seed_updated = 'Jy' + seed[2:]
print(seed_updated)

# Lists
# Lists are mutable

# Lists are compound data structures used to store comma-separated values

list1 = [4, 7, 3, 1]

# List can contain values of different data types, but usually values are of same type only
# List can be indexed and sliced too.

print(list1[0])

print(list1[2])

print(list1[-3:])

# This returns a shallow copy of list1

print(list1[:])

# List also support concatenation

print(list1 + [3, 7, 36, 2, 9])

# Lists are mutable

list1[2] = 34

print(list1)

# we can add values at end of list by .append() method

list1.append(23)
list1.append("Hi")

# we can replace some elements in a list with help of slicing

list1[2:4] = [3, 7]

print(list1)

# We can calculate length of both lists and strings by len() function

print(len(list1))

print(len(seed))

# Fibonacci Series
a, b = 0, 1  # variable assignment
while a < 10:
    print(a, end=",")
    a, b = b, a + b
