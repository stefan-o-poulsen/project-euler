# Solves Project Euler question 357
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2

def primesieve(N):
  """Sieve of Erastothenes, get primes up to N"""
  isprime = [False,False] + [True]*(N-1)
  for i in range(2,1+(N//2)): 
    if not isprime[i]: continue
    for j in range(2*i,N+1,i):
      isprime[j]=False
  primes = [prime for prime in range(len(isprime)) if isprime[prime]] 
  return primes,isprime

def main():
  # Set size of problem and generate primes
  N = 100000000
  (primes,isprime) = primesieve(N+1)
  # Again use a sieve
  isprimegen = [False]+[True]*(N+1)

  # We also need to consider 1 as a divisor
  primes = [1]+primes
  for d in range(1,N+1):
    # Loop over numbers where prime is a divisor
    for n in range(2*d,N+1,d):
      if isprimegen[n] and not isprime[d+n//d]: isprimegen[n] = False
  n = [i for i in range(len(isprimegen)) if isprimegen[i] and i<=N]
  print("sum is",sum(n))

if __name__ == '__main__':
  main()
