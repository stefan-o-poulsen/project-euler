# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from collections import Counter
primes = [2,3,5,7,11,13,17,19]
factors = Counter()
for N in range(2,21):
  n = N
  for p in primes:
    c = 0
    while n % p == 0:
      c += 1
      n //= p
    factors[p] = max([c,factors[p]])
s = 1
for key in factors.keys():
  s *= key**factors[key]
print(s)