# Numbers can be stored in varibles
pi = 3.14159
print(pi)

# You can do math with numbers
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

# If you combine with numbers, Python gets confused
# When displaying a string that contains numbers you must convert the numbers into strings
days_in_feb = 28
print(str(days_in_feb) + ' days in February')

# Numbers can be stored as strings
# Numbers stored as strings are treated as strings
first_num = '5'
second_num = '6'
print(first_num + second_num)

# The input function always returns strings
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
print(first_num + second_num)

# Numbers stored as strings must be converted to numeric values before doing math
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))
