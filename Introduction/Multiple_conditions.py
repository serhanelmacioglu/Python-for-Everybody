# CALCULATE CANADIAN SALES TAX
# If the province is Alberta or Nunavut charge 5%
# If the province is Ontario charge 13%

# If only one of the conditions will ever occur you can use a single if statement with elif

province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
print(tax)

# If the province is Alberta or Nunavut charge 5%
# If the province is Ontario charge 13%
# For all other provinces charge 15%

# When you use elif instead of multiple if statements you can add a default action

province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

# If multiple conditions cause the same action they can be combined into a single condition

province = input("What province do you live in? ")
tax = 0

if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

# If the province is Alberta, Nunavut, or Yukon charge 5%
# If the province is Ontario charge 13%
# For all other provinces charge 15%

# If you have a list of possible values to check, you can use the IN operator

province = input("What province do you live in? ")
tax = 0

if province in('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

# CALCULATE CANADIAN SALES TAX FOR CANADIAN RESIDENTS
# If the province is Alberta, Nunavut, or Yukon charge 5%
# If the province is Ontario charge 13%
# For all other provinces charge 15%
# Non Canadian residents do not pay sales tax

# If an action depends on a combination of conditions you can nest if statements

country = input("What country do you live in? ")

if country.lower() == 'canada':
    province = input("What province/state do you live in? ")
    if province in('Alberta', \
    'Nunavut', 'Yukon'):
         tax = 0.05
    elif province == 'Ontario':
         tax = 0.13
    else:
         tax = 0.15
else:
    tax = 0.0
print(tax)
