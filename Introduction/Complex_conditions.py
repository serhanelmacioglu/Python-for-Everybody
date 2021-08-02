# Requirements for honour roll
# A student makes honour roll if their average is >=85
# and their lowest grade is not below 70

gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)
 
if gpa >= .85:
     if lowest_grade >= .70:
         print('You made the honour roll')

# Sometimes you can combine conditions with AND instead of nesting if statements

gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll')

# If you need to remember the result of a condition check later in your code, use Boolean variables as flags

gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
    
# Somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
    print('You made honour roll')
