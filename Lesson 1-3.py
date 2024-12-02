"""
Name: William Nathan
Date: 12/2/24
Description: Strings
"""

# Review
name = "Starla" # a string literal
age = 5
# f-strings (formatted strings)
description = f"{name} likes wand toys and is {age}"

print(description)

# indexing - every character in a string has a location
# starting at 0 from the beginning or -1 from the end

#  0  1  2  3  4  5
#  S  t  a  r  l  a
# -6 -5 -4 -3 -2 -1

first_letter = name[0] # always use 0 if you don't know length
print(first_letter)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1*len(name)] # if you don't know the length
print(first_letter)

last_letter = name[-1] #always use if you don't know length
print(last_letter)
last_letter = name[len(name)-1]
print(last_letter)

# use [] to access a character not () - gives TypeError
# accessing a positive index that does not exist gives IndexError

try:
    print(name[20])
except IndexError:
    print("Out of Bounds")

# HW for Lesson 1 is 7.1.5 7.1.6
####################################
# Slicing - used to access 1 or more characters in a string
# Instead of name[0]+name[1]+name[2]

#first three letters
first_three = name[0]+name[1]+name[2]
print(first_three)
first_three = name[0:3]
print(first_three)

# Format
# string_name[start:stop:step] - none are technically required

word_one = "Adventure"

# What is the result of print(word_one[3:])?
# Try leaving out start

print(word_one[-1:-1:-1])
