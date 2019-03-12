import math
import cmath

a = float(input('Please Enter a:'))
b = float(input('Please Enter b:'))
c = float(input('please Enter c:'))

def quadratic(a, b, c):
    if not isinstance(a+b+c, (int, float)):
        raise TypeError('bad operand type of quadratic')

    if a == 0:
        if b == 0:
            if c == 0: # a = 0; b = 0; c = 0
                x = 'an arbitrary constant'
                return x
            else: # a = 0; b = 0; c != 0
                x = 'there is no solution'
                return x
        else: # a = 0; b, c != 0
            x = -(c / b)
            return x
    else:
        dert = b**2 - 4 * a * c
        if dert == 0:
            x1 = -b / (2 * a)
            x2 = -b / (2 * a)
            return x1, x2
        elif dert > 0:
            sqrt_dert = math.sqrt(dert)
            x1 = (-b + sqrt_dert) / (2 * a)
            x2 = (-b - sqrt_dert) / (2 * a)
            return x1, x2
        else:
             sqrt_dert = math.sqrt(-dert)
             real = -b / (2 * a)
             image = sqrt_dert / (2 * a)
             x1 = complex(real, image)
             x2 = complex(real, -image)

            # sqrt_dert = cmath.sqrt(-dert)
            # x1 = (-b + sqrt_dert) / (2 * a)
            # x2 = (-b - sqrt_dert) / (2 * a)

             return x1, x2

print('The solution to the equation is:', quadratic(a, b, c))
