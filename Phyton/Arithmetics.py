# Arithmetics Operations in Phyton
# Integers
print("=== Addition, Subtraction, Multiplication, Division, Modulus ===")
print('Addition: ', 1+2)
print('Subtraction: ', 5-1)
print('Multiplication: ', 6*3)
print('Division : ', 7/3)       # Result has an type float
print('Division: ', int(9/3))   # Result has an type integer
print('Division without the remainder   : ', 7//3)
print('Divsion without the remainder    :', 9//3)

print('Modulus  :',11 % 6)
print('Exponentiation   :', 7**3)

# Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number   :',1+1j)
print('Multiplaying complex numbers :',(1+1j)*(1-1j))
print('Matriks  :')

import numpy as num
arr = num.array([[2,3,1],[4,3,1]])
print((arr))


# Declare variable and assign a number data type
# declare variable a and b with assign value a number data type
a = 2
b = 4

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
mul = a * b
division = a / b
remainder = a % b
floor_division = a//b
exponential = a **b

# I should have used sum instead of total but sum is a built-in function -  try to avoid overriding built-in functions
print(total) # If you do not input label in pring, you never know is result is coming from form.
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', mul)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('==  Addition, Substraction, Multiplication, Division, Remainder ==')

# Declare values and organizing them together
num_one = 7
num_two = 3

# Arithmetic operations
totalValue = num_one + num_two
subtraction = num_one - num_two
product = num_one * num_two
div = num_one / num_two
remainderless = num_one // num_two

# Printing value with label
print('Total : ', totalValue)
print('Subtraction : ', subtraction)
print('Multiplication : ', product)
print('Division : ',div)
print('Remainder : ',remainderless)


import math
# Calculating area of a circle
radius = 9
area_of_the_circle = math.pi * radius **2
print('Area of the circle : ',area_of_the_circle)

# Calculating area of a rectangle
length = 11
width = 7
area_of_the_rectangle = length * width
print('Area of the rectangle : ', area_of_the_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.18
weight = mass * gravity
print('Weight : ',weight,'N')

# Calculate the density of a liquid
mass = 80 # in a Kilogram
volume = 0.075 # in cubic meter
density = mass / volume
print(density,'Kg/m^3')

#============================ COMPARISON OPERATORS ============================
print(4 > 2)
print(4 >= 2)
print(3 < 2)
print(4 < 6)
print(4 <= 7)
print(3 == 8/2)
print(3 != 5)

print(len('mango') == len('orange')) # False, Because char in the mango don't equal to char i the orange
print(len('mango') != len('avocado')) # True, Because char value in word mango and avocado don't equal
print(len('avocado') < len('orange')) # False,  Because char value in avocado gather than char in orange

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# In addition to the above comparison operator Python uses:
# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('2 is 2', 2 is 2) # [==]
print('1 is 3', 1 is not 3) # [!=]
print('K is Kevin Sanjaya', 'K' in 'Kevin Sanjaya')
print('J is Kevin Sanjaya', 'J' in 'Kevin Sanjaya')

#======================== LOGICAL OPERATORS =====================================
#Logical AND
print(4 > 1 and 4 > 5) # False
print(4 > 2 and 6 > 3) # True
#Logical OR
print(4 > 5 or 7 > 5) # True
print(8 < 2 or 5 < 1) # False 
#Logical Negation
print(not 4 > 2) # false
print(not False) # true
print(not True) # false