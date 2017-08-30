# Problem 50: Consecutive prime sum
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
N = 1000000
isprime = [True]*N
for i in range(2,N//2+1):
  for j in range(2*i,N,i):
    isprime[j] = False
primes = [p for p in range(len(isprime)) if isprime[p] and p>1]
primeset = set(primes)

maxcon,maxprime = 0,0
for i in range(len(primes)-1):
  s = primes[i]
  con = 1
  for j in range(i+1,len(primes)):
    if s>N:
      break
    con += 1
    s += primes[j]
    if s in primeset and con>maxcon:
      maxcon = con
      maxprime = s
print(maxprime)