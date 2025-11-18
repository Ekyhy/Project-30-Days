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