#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel

import json

person = { "firstName" : "Jane", "lastName" : "Doe", "age" : 5, "hasChildren": False, "titles": ['engineer', 'tester']}

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