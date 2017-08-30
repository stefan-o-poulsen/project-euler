# Problem 49: Prime permutations
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are 
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing 
# sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
import sys
isprime = [True]*10000
for i in range(2,len(isprime)):
  for j in range(2*i,len(isprime),i):
    isprime[j] = False
primes = [i for i in range(1000,len(isprime)) if isprime[i]]
primes.remove(1487)
primeset = set(primes)
for prime in primes:
  i=2
  for i in range(2,10000-prime-2*i,2):
    if prime+i in primeset and prime+2*i in primeset and sorted(str(prime))==sorted(str(prime+i)) and sorted(str(prime))==sorted(str(prime+2*i)):
      print(str(prime)+str(prime+i)+str(prime+2*i))
      sys.exit(0)
  
  
  