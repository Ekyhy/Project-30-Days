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