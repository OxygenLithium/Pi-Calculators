import math
import time
import sys

sys.set_int_max_str_digits(100000)

iterations = int(input("Enter the number of iterations "))

def arccot(x, prec_cof):
    x_exp = prec_cof//x
    n = 1
    rt = 0

    while n < 4*iterations:
        rt += x_exp//n
        n += 2
        x_exp = x_exp//(x*x)
        rt -= x_exp//n
        n += 2
        x_exp = x_exp//(x*x)
    first = rt + x_exp//n
    n += 2
    x_exp = x_exp//(x*x)
    second = rt - x_exp//n
    n += 2
    x_exp = x_exp//(x*x)
    return [first,second]

prec_cof = 10**(iterations*4+10)

start = time.time()
arctan1_5 = arccot(5,prec_cof)
arctan1_239 = arccot(239,prec_cof)
greater = 4*(4*arctan1_5[0]-arctan1_239[1])
lesser = 4*(4*arctan1_5[1]-arctan1_239[0])

end = time.time()

pi_approx = str((greater+lesser)//2)
pi_approx = "3." + pi_approx[1:]

lesser = str(lesser)
greater = str(greater)

rt = 0
running = True
while running:
    if lesser[rt:rt+1] == greater[rt:rt+1]:
        rt += 1
    else:
        running = False

print(end-start)
print(rt - 1)
print(pi_approx)
