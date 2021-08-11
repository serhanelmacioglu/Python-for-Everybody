# Error types are Syntax errors, Runtime errors and Logic errors.

# Syntax errors
# This code won't run at all
x = 42 
y= 206
if x == y
print('Success!')

# Runtime errors 
# This code will fail when run
x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This always runs on success or failure')

# Logic errors
#This code won't run at all
x = 206
y= 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))
