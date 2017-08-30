# Problem 46: Goldbach's other conjecture
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
primes = set([2])
twicesquares = set([2,8])
i=1
while True:
  i+=1
  twicesquares.add(2*i**2)
  i+=1
  twicesquares.add(2*i**2)
  isPrime = True
  for prime in primes:
    if i%prime==0:
      isPrime = False
      break
  if isPrime:
    primes.add(i)
    continue
  found=False
  for prime in primes:
    if i-prime in twicesquares:
      found=True
      break
  if not found:
    print(i)
    break

