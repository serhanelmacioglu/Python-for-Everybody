# Lists are collections of items
names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # Collections are zero-indexed

# Arrays are also collections of items
from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# What's the difference?
# Arrays: Numerical data types, must all be the same type
# Lists: Store anything, store any type

# Common operations
names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort() # Alphabetical order
print(names)

# Retrieving ranges
names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
#Start and end index
print(names)
print(presenters)

# Dictionaries
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

# What's the difference?
# Dictionaries: Key/Value pairs, Storage order not guaranteed
# Zero-based index, Storage order guaranteed
