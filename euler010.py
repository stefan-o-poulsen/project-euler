# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
N = int(2e6)
S = 0
prime = [True]*N
for i in range(2,N):
  if prime[i]:
    S += i
  for j in range(2*i,N,i):
    prime[j] = False
print(S)