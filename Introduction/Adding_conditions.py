# Example 1
price = (input ("How much did you pay? "))
price = float(price)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print ('Tax rate is: ' + str(tax))

# You can use this simple way in Python 3.X instead of the above strings
price = float(input ("How much did you pay? "))

if price >= 1.00:
    tax = .07
else:
    tax = 0
print (f"Tax rate is: {tax} ")

#Example 2
country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')
