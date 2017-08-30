# Problem 14: Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
N = 1000000
count = [None]*N
count[:1] = [0,1]

for n0 in range(2,N):
  n = n0
  chain = []
  while True:
    chain.append(n)
    if n%2==0:
      n //= 2
    else:
      n = 3*n+1
    if n<N and count[n] is not None:
      c = count[n]+1
      while chain:
        idx = chain.pop()
        if idx<N:
          count[idx] = c
        c += 1
      break
print(max(range(N),key=lambda x:count[x]))