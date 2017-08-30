# Problem 7: 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
N = 10001
primes = [2]
n = 1
while len(primes)<N:
  n += 2
  primes.append(n)
  for p in primes[:-1]:
    if n%p==0:
      primes.pop()
      break
print(primes[-1])