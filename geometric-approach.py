import math
from math import pi
from decimal import *

getcontext().prec=100000
iterations = int(input("Enter the number of iterations "))

def polygon_method(iterations):
    greater_perimeter = Decimal(6*math.sqrt(3))
    lesser_perimeter = Decimal(3*math.sqrt(3))
    
    i = 0
    while i < iterations:
        greater_perimeter = (2*greater_perimeter*lesser_perimeter)/(greater_perimeter+lesser_perimeter)
        lesser_perimeter = Decimal(greater_perimeter*lesser_perimeter).sqrt()
        i=i+1
    return (greater_perimeter+lesser_perimeter)/4

result = polygon_method(iterations)
print(result)




