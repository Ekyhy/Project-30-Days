# Day 2: 30 Days of python programming

first_name = 'Robert'
last_name = 'Yahya'
full_name = 'Robert Yahya'
country = 'Malaysia'
city = 'Selangor'
age = 19
year = 2007
is_married = False
is_true = True
is_light_on = True

first_name, last_name, age, is_married = 'Robert', 'Yahya', 19, False

# Check data type of all variable has been declare before
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Use len() for identify length of your first name
print(len(first_name))  #first name has been declare : Robert, 6 array : 'R','o','b','e','r','t'
print(len(last_name)) #last name has been declare :Yahya, 5 array: 'Y','a','h','y','a'
print(first_name  == last_name) #Return false because length of array is not equal

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two
total = num_one + num_two
print(type(total))
print(total)

# Subtract num_two and num_one
diff = num_two - num_one
print(type(diff))
print(diff)

# Divide num_one by num_two
division = num_one / num_two
print(type(division))
print(division)

# Use modulus division to find num_two by num_one
remainder = num_two % 2
print(type(remainder))
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_one
print(type(exp))
print(exp)

# Find floor division of num_one by num_two
floor_division = num_one // num_two
print(type(floor_division))
print(floor_division)

# The radius of a circle is 30 meters.
#   1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   3. Take radius as user input and calculate the area.

#  Task 1 : Calculate the area of a circle and assign the value to a variable name of area_of_circle
#       We know formula for calculate the area of a circle has
#          phi(22/7) of phi(3,14) multiply to the power of radius
#          formula :
#                   phi x radius^2

# Import library to use module formula (pi)
import math         

# Declare value radius
print(math.pi)
radius = 7

# Acction for solution
area_of_circle = math.pi * radius**2
print(int(area_of_circle))