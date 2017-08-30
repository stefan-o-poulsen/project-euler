# Problem 27: Quadratic primes
# Euler discovered the remarkable quadratic formula:
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when 
# n=40,40^2+40+41=40*(40+1)+41*n=40,40^2+40+41=40*(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41*n=41,41^2+41+41 
# is clearly divisible by 41.
# The incredible formula n^2−79*n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the 
# coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n^2+an+b, where |a|<1000 and |b|≤1000
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
# starting with n=0.

# Determine primes up to some cutoff and hope that its enough.
cutoff = 1000000
isprime = [True]*cutoff
for i in range(2,len(isprime)//2+1):
  for j in range(2*i,len(isprime),i):
    isprime[j] = False
primes = set([i for i in range(2,len(isprime)) if isprime[i]])
# Could be clever, but no need
prod,streak = 0,0
for b in range(2,1000):
  # Check n=0
  if b not in primes:
    continue
  # Check n=1
  for a in range(-1000,1000):
    if 1+a+b not in primes:
      continue
    n = 2
    while True:
      if n**2+a*n+b not in primes:
        break
      n += 1
    if n>streak:
      streak=n
      prod = a*b
print(prod)

