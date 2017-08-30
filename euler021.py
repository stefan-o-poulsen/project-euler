# Problem 21: Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
N = 10000
divsum = [0]*N
for d in range(1,N//2+1):
  for i in range(2*d,N,d):
    divsum[i] += d
n = 0
print(divsum)
for i in range(1,N):
  if divsum[i]<N and i==divsum[divsum[i]] and divsum[i]!=i:
    n += divsum[i]+divsum[divsum[i]]
print(n//2)