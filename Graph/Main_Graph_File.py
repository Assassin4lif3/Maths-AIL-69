import math
from Graph import discriminant_zeros as dz

# start
print('Your blank equation is ax² + bx + c = 0')

# inputs
a = int(input('Please provide value for a: '))
b = int(input('Please provide value for b: '))
c = int(input('Please provide value for c: '))

# calling discriminant_zeros
dz.discriminant_and_zeros(a,b,c)