#!/usr/bin/env python3

# thanks to @patloeber's youtube channel

# String - ordered, immutable, text

myString = "hello world"

myString = "I'm clever"  # escape character or use double quotes

myString = """ hello
world """  # """" for multiline sting
print(myString)

myString = """ hello \
world """  # """" for multiline sting but the escape char will avoid the new line
print(myString)

char = myString[3]
print(char)

# slicing
subString = myString[1:3]  # can leave out end index or start index
print(subString)

subString = myString[::2]  # copy every second char
print(subString)

subString = myString[::-1]  # -1 reverse copies :)
print(subString)

# concaternate
print(subString + myString)

# iterate
for i in myString:
    print(i)

# check presence
if "e" in myString:
    print("yes")

if "ell" in myString:
    print("yes")

# cooler stuff with strings
# get rid of whitespace
newString = myString.strip()
print(newString)

# convert case
newString = newString.lower()  # myString.upper()

# Check for start
print(newString.startswith("hell"))

# check for ending
print(newString.endswith("orld"))

# check for location of a char/substring
print(newString.find("o"))
print(newString.find("ll"))

# count number of occurences
print(newString.count("o"))

# replace text only if found
print(newString.replace("world", "universe"))


# convert to a list
myList = (
    newString.split()
)  # defualt delimiter is space, can provide  delimiter as argument
print(myList)

# list back to string
newString = " ".join(myList)  # uses the delimiter in the string - wowzers!
print(newString)

# formatting strings %, format, f-strings
var = "Tom"
myString = "the variable is %s" % var
print(myString)


# using format as opposed to c style %
var = 3.1415167
myString = "pi is {}".format(var)
print(myString)
var2 = 6
myString = "pi is {:.2f}, {}".format(var, var2)
print(myString)

# latest with the f-strings - evaluates at run time!
var = 3.1415167
myString = f"pi is {var}"
print(myString)
var2 = 6
myString = f"pi is {var}, {var2 * 3}"
print(myString)

# Slicing to get characters needed
s = "   hello   "
print(s[3:])

# strip to remove leading and trailing given characters
# default is space
s = " \n \t hello \n".strip("\n")
print(s)

# strip multiple chars
s = "www.example.com".strip("cmow.")
print(s)

# remove white spaces only one side
s = "      hello. worlds  ".lstrip()
print(s)

# if we just want to remove a prefix substring
s = "Alexander Dumas".lstrip("Alexander")
print(s)

# replace space with -
s = "string work in pyton".replace(" ", "_")
print(s)

# regex to replace substrings
import re

s = "string     methods                being    learnt"
s2 = re.sub("\s+", "-", s)  # this is better as it replaces all spaces
print(s2)

# split to break a string. Can specify the delimiter
s = "string    methods being  learnt"
# max split specifies how many parts to split
s2 = s.split(" ", maxsplit=1)
print(s2)

# join strings
list = ["string", "method", "in", "python"]
string = "".join(list)
print(string)

# uppercase
s = "abccd".upper()
s2 = s.lower()
print(s)
print(s2)
print(s.isupper())
print(s2.islower())

# swapcase
print(s2.swapcase())

# alpha check
print(s.isalpha())
print(s2.isnumeric())
print(s.isalnum())

# count
print(f"count of chrs is {s2.count('c')}")

# substring
s = "i wanna be awesome"
idx = s.find("wan", 2)  # alos has rfind - find from back
print(idx)
print(s[idx:])

# starts and endswith
print("Patrick".startswith("P"))

# partition - splits at the first occurence of a check string
# returns a tuple
# first item - beginning part of original string
# middle item - check string
# end item - ending part of the original sting
awstr = "Learning Python is awesome"
parts = awstr.partition("is")
print(parts)

# center , ljust, and rjust
center = awstr.center(35, "-")
print(center)

# f string to format - you this already i hope!

# zfill - returns string of given length with zero fill
# number formatting
s = "42".zfill(5)
print(s)
