# Problem 47: Distinct primes factors
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
primes = [2]
i=2
primefactors={}
while True:
  i+=1
  pf = set([])
  i0=i
  for prime in primes:
    if prime>i0:
      break
    f=1
    while i0%prime==0:
      f*=prime
      i0//=prime
    if f>1:
      pf.add(f)
  if i0==i:
    primes.append(i0)
  if len(pf)==4:
    primefactors[i]=pf
  else:
    continue
  testset = set([])
  for j in range(4):
    if i-j in primefactors:
      testset = testset.union(primefactors[i-j])
    else:
      break
  if len(testset)==16:
    print(i-3)
    break