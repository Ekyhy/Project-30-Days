# ========== CREATING A STRING ================
letter = 'p'        # A srings could be a single character
print(letter)       # P
print(len(letter))  # 1

greeting = 'Hello, World!' # String could be made using a single ('...') or double quote ("....")
print(greeting)
print(len(greeting)) 

sentence = 'I hope you are enjoying for 30 day of Python Programming Challenges'
print(sentence)
print(len(sentence))


# ====================== STRINGS CONCATENATION ===========================

first_name = 'Robert'
last_name = 'Victor'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# ==================== Escape Sequences in Strings ========================

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

print('Do you enjoying the Python Challenges 30 Days Program. \nAre you?')
print('Days\tTopics\tExercise')
print('Day 1\t5\t5')
print('Day 2\t6\t6')
print('Day 4 \t6\t23')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"Hello, World"')

# We can see the output 

# ============= STRING FORMATING ====================
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
# we can use %s
first_name = 'Roberto'
last_name = 'Frionto'
language = 'Python'
format_string = 'I am %s %s. Now I study %s' %(first_name,last_name,language)
print(format_string)

# Strings and Numbers
radius = 11
pi = 3.14
area = pi * radius **2
format_string = 'The area of circle with a radius %d is %.2f.' %(radius,area)
print(format_string)

python_librares = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
format_string = 'The following are python libraies:%s' % (python_librares)

print(format_string)

# New Style String Formatting (str.format)
first_name = 'Roberto'
last_name = 'Frionto'
language = 'Python'
format_string = 'I am {} {}. No, learing {}'.format(first_name,last_name,language)
print(format_string)

# Declare value a and b
a = 8
b = 5

print('{} + {} = {}'.format(a,b,a + b))
print('{} - {} = {}'.format(a,b, a - b))
print('{} * {} = {}'.format(a,b, a * b))
print('{} / {} = {:.2f}'.format(a,b, a / b))
print('{} % {} = {}'.format(a,b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a,b, a ** b))

# ==================== String Interpolation ===============
a = 4
b = 2
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b :.2f}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')


# ================== Strings as Sequences Characters ============
# Python Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing Characters in Strings by Index from left to right
print("\n")
language = 'Python'
first_latter = language[0]
print(first_latter)
second_latter = language[1]
print(second_latter)
third_latter = language[2]
print(third_latter)
# Accessing last character
last_index = len(language)-1
last_latter = language[last_index]
print(last_latter)

# Accessing Characters in Strings by Index from right to left
language = 'Python'
last_latter = language[-1]
print('\n',last_latter)
second_latter = language[-2]
print(second_latter)

# Slicing Python Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reversing Strings
greeting = 'Hello, World'
print(greeting[::-1])


# ==================== STRINGS METODS =====================
# Capitalize
challenges = 'thirty days of python'
print(challenges.capitalize())
# Count
challenges = 'thirty days of python'
print(challenges.count('y'))
print(challenges.count('y',6,8))
print(challenges.count('day'))
# endswith
challenge = 'thirty days of python'
print(challenge.endswith('on'))   
print(challenge.endswith('ys')) 
# expandtabs
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  
print(challenge.expandtabs(10)) 
# find
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th')) 
# rfind
challenge = 'thirty days of python'
print(challenge.rfind('y'))  
print(challenge.rfind('th')) 
# format
first_name = 'Roberto'
last_name = 'Frionto'
language = 'Python'
format_string = 'I am {} {}. No, learing {}'.format(first_name,last_name,language)
print(format_string)
a = 8
b = 5
print('{} + {} = {}'.format(a,b,a + b))
print('{} - {} = {}'.format(a,b, a - b))
print('{} * {} = {}'.format(a,b, a * b))
print('{} / {} = {:.2f}'.format(a,b, a / b))
print('{} % {} = {}'.format(a,b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a,b, a ** b))
# index
challenge = 'thirty days of python'
sub_strings = 'da'
print(challenge.index(sub_strings))  

# rindex
challenge = 'thirty days of python'
sub_strings = 'da'
print(challenge.rindex(sub_strings))  
print(challenge.rindex('thon',9))
# isalnum
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) 
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'thirty days of python'
print(challenge.isalnum())
challenge = 'thirty days of python 2019'
print(challenge.isalnum()) 
# isalpha
challenge = 'thirty days of python'
print(challenge.isalpha())
challenge = 'ThirtyDaysOfPython'
print(challenge.isalpha())
challenge = '345'
print(challenge.isalpha())
#isdecimal
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
#isdigit
challenge = "Thirty"
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
challenge = 'j\tyojb'
print(challenge.isdigit())
# isnumeric
num = '10'
print(num.isnumeric()) 
num = '\u00BD'
print(num.isnumeric()) 
num = '10.5'
print(num.isnumeric())
# isidentifier
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
# islower
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'ThirtyDaysofPython'
print(challenge.islower())
# isupper
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
# join
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ','.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
# strips
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
# replace
challenge = 'thirty days of python'
print(challenge.replace('python','ruby')) # thirty days of ruby
# split
challenge = 'thirty days of python'
print(challenge.split()) 
challenges = 'thirty days of python'
print(challenges.split(', ')) 
# title
challenge = 'thirty days of python'
print(challenge.title())
# swapcase
challenge = 'thirty days of python'
print(challenge.swapcase())  
# startwith
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False