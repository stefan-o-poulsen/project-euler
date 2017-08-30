# Problem 32: Pandigital products
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit 
# number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 
# pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
from itertools import permutations
prod = set([])
digits = [str(s) for s in range(1,10)]
digitset = set(digits)
for NLHS in range(2,len(digits)):
  for LHS in permutations(digits,NLHS):
    RHS = digitset-set(LHS)
    for l in range(1,NLHS//2+1):
      p = int(''.join(LHS[:l]))*int(''.join(LHS[l:]))
      strp = str(p)
      if len(strp)==len(RHS) and set([s for s in strp])==RHS:
        prod.add(p)
print(sum(list(prod)))
