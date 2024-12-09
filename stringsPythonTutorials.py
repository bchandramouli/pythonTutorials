#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel

#String - ordered, immutable, text

myString = "hello world"

myString = 'I\'m clever' #escape character or use double quotes

myString = """ hello
world """ # """" for multiline sting
print(myString)

myString = """ hello \
world """ # """" for multiline sting but the escape char will avoid the new line
print(myString)

char = myString[3]
print(char)

#slicing
subString = myString[1:3] # can leave out end index or start index 
print(subString)

subString = myString[::2] #copy every second char
print(subString)

subString = myString[::-1] # -1 reverse copies :)
print(subString)

#concaternate
print(subString+myString)

#iterate
for i in myString:
	print(i)

#check presence
if 'e' in myString:
	print('yes')

if 'ell' in myString:
	print('yes')

#cooler stuff with strings
#get rid of whitespace
newString = myString.strip()
print(newString)

#convert case
newString = newString.lower() #myString.upper()

#Check for start
print(newString.startswith("hell"))

#check for ending
print(newString.endswith("orld"))

#check for location of a char/substring
print(newString.find('o'))
print(newString.find('ll'))

# count number of occurences 
print(newString.count('o'))

#replace text only if found
print(newString.replace("world", "universe")) 


#convert to a list
myList = newString.split() #defualt delimiter is space, can provide  delimiter as argument
print(myList)

#list back to string
newString = ' '.join(myList) #uses the delimiter in the string - wowzers!
print(newString)

#formatting strings %, format, f-strings
var = "Tom"
myString = "the variable is %s" % var
print(myString)


#using format as opposed to c style %
var = 3.1415167
myString = "pi is {}". format(var)
print(myString)
var2 = 6
myString = "pi is {:.2f}, {}". format(var, var2)
print(myString)

#latest with the f-strings - evaluates at run time!
var = 3.1415167
myString = f"pi is {var}"
print(myString)
var2 = 6
myString = f"pi is {var}, {var2 * 3}"
print(myString)