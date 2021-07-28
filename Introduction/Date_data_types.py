# We often need current date and time when logging errors and saving data

# To get current date and time
# we need to use the datetime library
from datetime import datetime
current_date = datetime.now()
# the now function returns a datetime object
print('Today is: ' + str(current_date))

# There are functions you can use with datetime objects to manipulate dates
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))
# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: '+ str(yesterday))

# Use date functions to control date formating
from datetime import datetime
current_date = datetime.now()
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# Sometimes you receive the date as a string and need to convert it to a datetime object
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('Birthday: ' + str(birthday_date))

# Converting it to a datetime allows you to use the date functions
from datetime import datetime, timedelta
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('Birthday: ' + str(birthday_date))
# timedelta is used to define the day before birthday
one_day =timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
