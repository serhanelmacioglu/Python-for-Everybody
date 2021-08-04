# Adding collections, lists and dictionaries to code

christopher = {}
christopher['first'] = 'Christopher'
christopher['last'] = 'Harrison'

susan = {}
susan['first'] = 'Susan'
susan['last'] = 'Harrison' 

people = []
people.append(christopher)
people.append(susan)
people.append({
    'first' : 'Bill', 'last': 'Gates'
    })

print(people)
