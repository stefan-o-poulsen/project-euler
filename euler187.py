# Solution to Project Euler question 187
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2

Nmax = 100000000

def primesieve(N):
  """Sieve of Erastothenes, get primes up to N"""
  isprime = [False,False] + [True]*(N-1)
  for i in range(2,1+(N//2)): 
    if not isprime[i]: continue
    for j in range(2*i,N+1,i):
      isprime[j]=False
  primes = [prime for prime in range(len(isprime)) if isprime[prime]] 
  return primes

# Get all primes up to Nmax
primes = primesieve(Nmax)
# And count all prime factors
num_factors = [0]*Nmax
for p in primes:
  for num in range(p,Nmax,p):
    n = num
    while n % p == 0:
      n = n//p
      num_factors[num]+=1
c=0
for i in num_factors:
  if i==2:
    c+=1

print("Number of composite integers: ",c)
