# Write a Python Program to implement python maths function/method (pi, e, sqrt, ceil,floor, pow, fabs, sin, cos, tan) using math module.

import math

# printing the value of PI
print(f"the value of pi is{math.pi}")

# printing Eulers number
print(f"the Euler constant is {math.e}")

# finding square root
print(f"the square root of 625 is {math.sqrt(625)}")

# round of by ceil and floor
print(f"546.7856 will get convert to \"{math.ceil(546.7856)}\" by ceil function and \"{math.floor(546.7856)}\" by floor function in the math module")

# pow function
print(f'5 raise to power 10 is {math.pow(5,10)}')

#Fabs function
print(f'-456546 will get convert to {math.fabs(-456546)} by fabs() function')

# sin function
print(f'the sine of 45 {math.sin(math.radians(45))}')

# cos function
print(f'the cosine of 45 {math.cos(math.radians(45))}')

# tan function
print(f'the tangent of 45 {math.tan(math.radians(45))}')

# Output
# the value of pi is3.141592653589793
# the Euler constant is 2.718281828459045
# the square root of 625 is 25.0
# 546.7856 will get convert to "547" by ceil function and "546" by floor function in the math module
# 5 raise to power 10 is 9765625.0
# -456546 will get convert to 456546.0 by fabs() function
# the sine of 45 0.7071067811865476
# the cosine of 45 0.7071067811865476
# the tangent of 45 0.9999999999999999