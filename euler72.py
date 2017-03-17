# Solves Project Euler question 72
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2
import math

def gcd(a,b):
	"""Euclidean algorithm for greatest common divisor"""
	while b != 0:
		t = b 
		b = a % b 
		a = t 
	return a

lim0 = (1,3)
lim1 = (1,2)
T0 = lim0[0]/lim0[1]
T1 = lim1[0]/lim1[1]

def main():
  dmax = 12000
  # Loop over all possible denominators
  fracs = {}
  for d in range(1,dmax+1):
    # Find lower limit
    n = math.ceil(T0*d)
    while n<=T1*d:
      nn = n
      dd = d
      while True:
        div = gcd(nn,dd)
        if div==1: break
        nn /= div
        dd /= div
      if not fracs.get((nn,dd)):
        fracs[(nn,dd)] = True
      n += 1
  # We are also counting 1/2 and 1/3, so correct
  S = len(fracs)-2
  print("Number of fractions is",S)

if __name__ == '__main__':
	main()