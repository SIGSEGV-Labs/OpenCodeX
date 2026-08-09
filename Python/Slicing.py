"""
This python program implements strings in python and performs indexing on the strings.

"""

# Take string input from the user:

string = input("Enter any string: ")

# First character of the string:

print(string[0])

# Second character of the string:

print(string[1])

# Last character of the string:

print(string[-1])

# Second last character of the string:

print(string[-2])

# Slicing:

print(string[0:3])

print(string[2:])

print(string[:3])

print(string[len(string)-1])

print("a" in string)
print("sil" in string)

print(string[1:5:1])
