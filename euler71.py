# Solves Project Euler question 71
# Stefan Othmar Poulsen, 2017
import math

def gcd(a,b):
	"""Euclidean algorithm for greatest common divisor"""
	while b != 0:
		t = b 
		b = a % b 
		a = t 
	return a

def main():
  dmax = 1000000
  N = 3
  D = 7
  # T is our target in floating point
  T = float(N)/D

  bestmatch = bestN = bestD = 1
  for d in range(1,dmax+1):
    # this is our new numerator
    n = math.ceil(T*d)
    # Reduce numerator until we are below our target
    while n>T*d and n>0:
      n -= 1.0
    t = T-n/d
    # t is positive, so we are looking for the minimum
    if t < bestmatch:
      # The fraction we have determined may be identical to the target
      n = int(n)
      while True:
        div = gcd(n,d)
        if div==1: break
        n /= div
        d /= div
      if n!=N and d !=D:
        bestmatch = t
        bestN = n
        bestD = d
  print("Fraction is ",bestN,'/',bestD)

if __name__ == '__main__':
	main()