#!/usr/bin/env python3

#thanks to @patloeber's youtube channel

import json

person = {"name" : "Jane", "age" : 5, "hasChildren": False, "titles": ['engineer', 'tester']}

# python objects to json types mapping
# dictionary -> Object
# list, tuple -> array
# str -> string
# int, long, float -> naumber
# True -> true
# False -> false
# None -> null

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
	json.dump(personJSON, file, indent=4)

# convert JSON string back to a python dictionary
person = json.loads(personJSON)
print(person)

with open('person.json', 'r') as file:
	person = json.load(file)
	print(person)

class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age

user = User('Max', 27)

def encode_user(o):
	if isinstance(o, User):
		return {'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
	else:
		raise TypeError('Object of type User is not JSON serializable')

# use an encoder function to serialize it correctly
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder
class UserEncoder(JSONEncoder):
	def default(self, o):
		if isinstance(o, User):
			return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
		else:
			raise TypeError('Object of type User is not JSON serializable')

# use the UserEncode class with default overridden
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

# Another way to do it by calling the class function on the user
userJSON = UserEncoder().encode(user)
print(userJSON)

# decode back
user = json.loads(userJSON)
print(user)

# add a function to deserialize
def decode_user(dct):
	if User.__name__ in dct:
		return User(name = dct['name'], age = dct['age'])
	return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)