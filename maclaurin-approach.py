import math
from decimal import *

getcontext().prec=100

iterations = int(input("Enter the number of iterations "))

def infseries_method(iterations):
    running_total = Decimal(0)
    i = Decimal(1)
    positive = True
    while i < (iterations+1):
        if positive == True:
            running_total = running_total + 4/(2*i-1)
            positive = False
        else:
            running_total = running_total - 4/(2*i-1)
            positive = True
        i = i+1
    return running_total

result = infseries_method(iterations)

print(result)

result_current_digit = result//1
pi_current_digit = pi//1

matches = 0
while result_current_digit == pi_current_digit:
    matches = matches+1
    result = (10*result)%10
    pi = (10*pi)%10
    result_current_digit = result//1
    pi_current_digit = pi//1

print(matches)

