# Problem 34: Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
Nupper = 10000000
from math import factorial
fac = [int(factorial(i)) for i in range(0,10)]
S = 0
for s in range(10,Nupper+1):
    dsum = sum([fac[int(i)] for i in str(s)])
    if s==dsum:
      S+=dsum
print(S)