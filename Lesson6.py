"""
Name: William Nathan
Date: 12/6/24
Description:
"""



# upper case
name = "starla"
print(name.upper()) # this prints STARLA
print(name) # this prints starla - name didn't change

name = name.upper() # this will replace name with STARLA
print(name)

# lower case
name = "FRANKLIN"
print(name.lower()) # prints franklin

# title case
sentence = "FRANKLIN LEAVE MILLIE ALONE"
print(sentence.title())

# swap case
word = "ViOlIn"
print(word.swapcase())

# strip
school = "    Oregon State     University      "
print(school.strip())

# find: returns index of first occurence, -1 if now found

print("Oregon State University".find("go"))

#########################################################

# Boolean checks
print("B".isupper())
print("B".islower())
print("B".isalpha())
print("B".isalnum()) # letter or number
print("B".isdigit())