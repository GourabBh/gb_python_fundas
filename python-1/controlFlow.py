# Input from user

from turtle import st


# x = int(input("Enter a number: "))

# if x < 0:
#     x = 0
#     print("Negative made to zero")
# elif x == 0:
#     print("Number is zero")
# elif x == 1:
#     print("Number is one")
# else:
#     print("Number greater than one!")

# elif -> else-if, else is optional

# ------------------------------------------
# For loop
words = ['cat', 'window', 'oscillations']

for word in words:
    for letter in word:
        print(letter, end="-")
    print()

# Dictionaries in python

users = {'Ram': 'active', 'Sam': 'inactive', 'Thomas': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Better create a new collection

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# The range function

for i in range(10):
    print(i, end=",")
print()  # This will always add a new line


for i in range(-34, -734, -50):
    print(i, end="@")
