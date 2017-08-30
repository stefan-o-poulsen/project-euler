# Problem 35: Circular primes
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.There are # thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# Generate all primes
N = 1000000
isprime = [True]*N
for i in range(2,N//2+1):
  for j in range(2*i,N,i):
    isprime[j] = False
primes = [str(p) for p in range(2,len(isprime)) if isprime[p]]
count = 0
# Weed out obvious cases
for i in range(len(primes)-1,-1,-1):
  S = primes[i]
  if len(S)==1:
    count += 1
    primes.pop(i)
    continue
  for s in S:
    if s in set(['0','2','4','5','6','8']):
      primes.pop(i)
      break
# Rotate remaining prime strings
for prime in primes:
  count += 1 
  for _ in range(len(prime)):
    prime = prime[1:]+prime[0:1]
    if ''.join(prime) not in primes:
      count -= 1
      break
print(count)  
  