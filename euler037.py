# Problem 37: Truncatable primes
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Can't find an  upper bound, so choose arbitrarily
isprime = [True]*1000000
for i in range(2,len(isprime)//2+1):
  for j in range(2*i,len(isprime),i):
    isprime[j] = False
primes = [i for i in range(2,len(isprime)) if isprime[i]]
primeset = set(primes)
S = []
for prime in primes[4:]:
  s = str(prime)
  allprime = True
  for i in range(1,len(s)):
    if int(s[:-i]) not in primeset or int(s[i:]) not in primeset:
      allprime = False
      break
  if allprime:
    S.append(prime)
    if len(S)==11:
      break
print(sum(S))